from owlready2 import *
import json
from datetime import date, datetime

path_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
sys.path.append(path_dir)

from src.config import config
from src.utils import typeData
import api.services.spqrqlQueries.queries as queries
import api.services.spqrqlQueries.utils as utils


class SparqlQueries:
    def __init__(self) -> None:
        self.path = config['path']
        my_world = World()
        #path to the owl file is given here
        my_world.get_ontology(self.path).load()
        #sync_reasoner(my_world)  #reasoner is started and synchronized here
        self.graph = my_world.as_rdflib_graph()

    # получение публикаций по названию
    def getDataByNames(self, title, typeSearch):
        prop1, prop2 = utils.getDataByNameProperty(typeSearch)

        title = title.lower()
        if title != "":
            query = queries.getDataByNameQuery(prop1, title)
        else:
            query = queries.getAllDataQuery(prop1, prop2)
        
        resultsList = self.graph.query(query)

        response = []

        for item in resultsList:
            title = str(item['title'].toPython())
            title = re.sub(r'.*#',"", title)
            print(title)
            print()
            themes, authors, url, citations, resourses, views, dowloads, datePublished = self.getTitleThemesAndAuthors(title, typeSearch)
            
            if themes != [] or authors != []:
                response.append({'title' : title, 'themes': themes, 'authors': authors, 'url': url, 'citations': citations, 'resourse': resourses, 'views': views, 'dowloads': dowloads, 'datePublished': datePublished})
        
        print(response)
        return response

     # получаем темы и авторов у книги или статьи
    def getTitleThemesAndAuthors(self, title, typeSearch):
        prop1, prop2, prop3, prop4, prop5, prop6, prop7, prop8 = utils.getTitleThemesAndAuthorsProperty(typeSearch)
 
        if typeSearch is typeData.Sites:
            query = queries.getPropertyForWebResourseQuery(prop1, prop3, prop5, title) # тут надо для начала сделать агента для парсинга веб ресурсов
        else:
            query = queries.getPropertyForBookOrArticleQuery(prop1, prop2, prop3, prop4, prop5, prop6, prop7, prop8, title)
        #print("Запрос: ", query)

        themes = []
        authors = []
        url_list = []
        citations = []
        resourses = []
        views = []
        dowloads = []
        datePublished = []

        try:
            result = self.graph.query(query)
        except Exception:
            print("тут ошибка: ", title)
        else:
            for item in result:
                utils.addItemInList(item, 'theme', themes)
                utils.addItemInList(item, 'url', url_list)
                utils.addItemInList(item, 'resourse', resourses)
                utils.addItemInList(item, 'views', views)
                utils.addItemInList(item, 'dowloads', dowloads)
                utils.addItemInList(item, 'datePublished', datePublished)

                if typeSearch is not typeData.Sites:
                    utils.addItemInList(item, 'author', authors)
                    utils.addItemInList(item, 'numberOfCitations', citations)

        return themes, authors, url_list, utils.getListWithMaxElem(citations), resourses, utils.getListWithMaxElem(views), utils.getListWithMaxElem(dowloads), datePublished

    # получение авторов по названию
    def getAuthorByNames(self, name):
        name = name.lower()
        
        query = queries.getAuthorByNameQuery(name)
        result = self.graph.query(query)

        response = []

        for item in result:
            author = str(item['author'].toPython())
            author = re.sub(r'.*#',"", author)
            print(author)
            print()
            themes, items = self.getAuthorThemesAndData(author)
            
            if not (themes == [] or items == []):
                response.append({'author' : author, 'themes': themes, 'items': items})
        
        print(response)
        return response

    # получаем темы и публикации у автора
    def getAuthorThemesAndData(self, name):
        prop1, props2 = utils.getAuthorThemesAndDataProperty()
        queryGetThemes = queries.getAuthorThemesQuery(name, prop1)

        themes = []
        items = []

        # получаем темы
        try:
            resultThemes = self.graph.query(queryGetThemes)
        except Exception:
            print("тут ошибка: ", name)
        else:
            for item in resultThemes:
                utils.addItemInList(item, 'theme', themes)
        
        # получаем публикации
        for prop in props2:
            queryGetItems = queries.getAuthorItemsQuery(name, prop)
            try:
                resultItems = self.graph.query(queryGetItems)
            except Exception:
                print("тут ошибка: ", name)
            else:
                for item in resultItems:
                    utils.addItemInList(item, 'item', items)
        print(themes, items)
        return themes, items

def main():
    ont = SparqlQueries()
    #ont.getDataByNames("Палино", typeData.Books)
    ont.getAuthorByNames("по")


if __name__ == "__main__":
    main()