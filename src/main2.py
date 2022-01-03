import ontology.ontology as ontology
import parserAgent.parserAgent as parserAgent
import utils
from config import config

def main():
    path = config['path']

    ont = ontology.Ontology(path)
    #ont.create_ontology()
    #return
    
    #agent = parserAgent.MobileAgent(utils.parseResource.GoogleSearch, "палинология")
    agent = parserAgent.MobileAgent(utils.parseResource.GoogleBooks, "палинология")
    #agent = parserAgent.MobileAgent(utils.parseResource.MicrosoftAcademic, "палинология")
    #agent = parserAgent.MobileAgent(utils.parseResource.CyberLeninka, "палинология")
    #agent = parserAgent.MobileAgent(utils.parseResource.PubMed, "palynology")
    #agent = parserAgent.MobileAgent(utils.parseResource.Frontiersin, "palynology")
    result = agent.start()
    #print(result)
    ont.recordingNewItemInOntology(result)

if __name__ == "__main__":
    main()
