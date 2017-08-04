import wikipedia

hotels = wikipedia.page("List of hotels in the United States")

f = open('hotels.txt', 'w')

for i in range(0,len(hotels.links)):
    f.write(hotels.links[i]+";")

f.close()



