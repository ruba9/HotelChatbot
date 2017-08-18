from urllib.request import urlopen
import pysolr

solr = pysolr.Solr('http://localhost:8983/solr/bot/')




def byName(name):

    results = solr.search('name: {0}'.format(name))
    # print("Saw {0} result(s).".format(len(results)))
    Hotels = []
    for hotel in results.docs:
        Hotels.append(hotel)
    return Hotels



def byPrice(price):
    results = solr.search('price: [{0} TO {1}]'.format(price-10, price+10))
    print("Saw {0} result(s).".format(len(results)))
    Hotels = []
    for hotel in results.docs:
        Hotels.append(hotel)
    return Hotels

def byRegion(region):
    results = solr.search('region: {0}'.format(region))
    print("Saw {0} result(s).".format(len(results)))
    Hotels = []
    for hotel in results.docs:
        Hotels.append(hotel)
    return Hotels

def byRegionAndPrice(region, price):
    results = solr.search('region: {0} and price: [{1} TO {2}]'.format(region, price-10, price+10))
    print("Saw {0} result(s).".format(len(results)))
    Hotels = []
    for hotel in results.docs:
        Hotels.append(hotel)
    return Hotels

