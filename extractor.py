import textrazor


def detectHotel(sen):
    textrazor.api_key = "90a95f0c5eb5756e92bc9594dababf817eb558a64579392b7e64e763"

    client = textrazor.TextRazor(extractors=["entities", "topics"])
    response = client.analyze(sen)
    entities=response.entities()

    import re
    OBJFINDER=dict()
    for tuples in entities:
              type= tuples.freebase_types
              Enviroment = str((re.findall("/([A-Za-z]+)/", str(type)))).replace('[\'',"").replace('\']',"")
              objects=tuples.id
              if len(Enviroment) == 0:
                  Enviroment="UN"
              OBJFINDER[str(Enviroment)]=objects


    if "location" in OBJFINDER:
        return OBJFINDER["location"]
    else :
        return "NF"



