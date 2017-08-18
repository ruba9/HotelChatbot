import pandas as pd
import json
import re
import os, sys
import xlrd
from bs4 import BeautifulSoup

linker = 0
old = 0
counter = 0
lastreviewlist=list()



def checker(i):
    global Listd
    global Frame
    global linker
    global newlenght
    global counter
    global lastreviewlist
    global List
    counter += 1
    linker = counter - newlenght

    if linker != orginalLength:
        print(newlenght, "******")
        if "Service" not in js["Reviews"][linker]["Ratings"]:
            List.append(0)
        else:
            List.append(str(BeautifulSoup(js["Reviews"][linker]["Ratings"]["Service"],"html.parser").get_text))

        if "Cleanliness" not in js["Reviews"][linker]["Ratings"]:
            List.append(0)
        else:
            List.append(BeautifulSoup(js["Reviews"][linker]["Ratings"]["Cleanliness"],"html.parser").get_text)

        if "Overall" not in js["Reviews"][linker]["Ratings"]:
            List.append(0)
        else:
            List.append(BeautifulSoup(js["Reviews"][linker]["Ratings"]["Overall"],"html.parser").get_text)

        if "Value" not in js["Reviews"][linker]["Ratings"]:
            List.append(0)
        else:
            List.append(BeautifulSoup(js["Reviews"][linker]["Ratings"]["Value"],"html.parser").get_text)

        if "Sleep Quality" not in js["Reviews"][linker]["Ratings"]:
            List.append(0)
        else:
            List.append(BeautifulSoup(js["Reviews"][linker]["Ratings"]["Sleep Quality"],"html.parser").get_text)

        if "Rooms" not in js["Reviews"][linker]["Ratings"]:
            List.append(0)
        else:
            List.append(BeautifulSoup(js["Reviews"][linker]["Ratings"]["Rooms"],"html.parser").get_text)

        if "Location" not in js["Reviews"][linker]["Ratings"]:
            List.append(0)
        else:
            List.append(BeautifulSoup(js["Reviews"][linker]["Ratings"]["Location"],"html.parser").get_text)

        if "AuthorLocation" not in js["Reviews"][linker]:
            List.append(0)
        else:
            List.append(BeautifulSoup(js["Reviews"][linker]["AuthorLocation"],"html.parser").get_text)

        if "Title" not in js["Reviews"][linker]:
            List.append(0)
        else:
            List.append(BeautifulSoup(js["Reviews"][linker]["Title"],"html.parser").get_text)

        if "Author" not in js["Reviews"][linker]:
            List.append(0)
        else:
            List.append(BeautifulSoup(js["Reviews"][linker]["Author"],"html.parser").get_text)

        if "ReviewID" not in js["Reviews"][linker]:
            List.append(0)
        else:
            List.append(js["Reviews"][linker]["ReviewID"])
        if "Content" not in js["Reviews"][linker]:
            List.append(0)
        else:
            List.append(BeautifulSoup(js["Reviews"][linker]["Content"],"html.parser").get_text)

        if "Date" not in js["Reviews"][linker]:
            List.append(0)
        else:
            List.append(BeautifulSoup(js["Reviews"][linker]["Date"],"html.parser").get_text)
        Frame.loc[i] = List
        List = list()

    else:
            lastreviewlist.append(js["Reviews"][linker-1]["ReviewID"])





list_of_hotels=list()
def listhotel(hotel, enter):
    list_of_hotels.append(BeautifulSoup(hotel["HotelInfo"]["Name"],"html.parser").get_text)
    list_of_hotels.append(BeautifulSoup(hotel["HotelInfo"]["HotelURL"],"html.parser").get_text)
    list_of_hotels.append(BeautifulSoup(hotel["HotelInfo"]["Price"],"html.parser").get_text)
    list_of_hotels.append(BeautifulSoup(hotel["HotelInfo"]["Address"],"html.parser").get_text)
    list_of_hotels.append(BeautifulSoup(hotel["HotelInfo"]["HotelID"],"html.parser").get_text)
    list_of_hotels.append(BeautifulSoup(hotel["HotelInfo"]["ImgURL"],"html.parser").get_text)
    list_of_hotels[enter] = list(list_of_hotels[enter:len(list_of_hotels)])
    del(list_of_hotels[enter+1:])


numberofhotel = len(list_of_hotels)
cols = ["name", "Hotelurl", "price", "address", "hotelid", "imgurl"]
hotellist = pd.DataFrame(columns=cols, index=range(0, int(numberofhotel)))



def WriteListofHotels(hotel):
    global hotellist
    hotelcounter=0
    for hotelname in hotel:
             print(hotelname) #testing
             hotellist.loc[hotelcounter]=hotelname
             hotelcounter+=1







folder = "/Users/zaid_zaghloul/Desktop/filesdealer/json"
listofdir = os.listdir(folder)[:100]

Flag = True
maxprevlength = 0
newlenght = 0
data = 10000
counter = 0
enter = -1
filejsonlist=list()

for filejson in listofdir:

    file = open(folder + "/" + filejson, mode="r")
    st = file.read()
    js = json.loads(st)
    length = 0
    col1s = re.findall("[a-zA-Z]+", str(js["Reviews"][0].keys()))[2:]
    col2s = re.findall("[a-zA-Z]+", str(js["Reviews"][0]["Ratings"].keys()))[2:]
    TotalCol = col2s + col1s
    del (TotalCol[TotalCol.index("Ratings")])
    TotalCol[4:6] = ["SleepQuality"]
    linker = 0
    counter = 0
    coltotal = len(TotalCol)
    List = list()

    if Flag:
        Frame = pd.DataFrame(columns=TotalCol, index=range(0, data))
        Flag = False
    if len(TotalCol) is 13:
        filejsonlist.append("/" + filejson)
        enter += 1
        listhotel(js, enter)
        print(file)
        maxprevlength = newlenght
        length = len(js["Reviews"])
        orginalLength=len(js["Reviews"])
        if maxprevlength < length or length<maxprevlength:
            newlenght = maxprevlength + length
            linker = newlenght
            counter=newlenght
            old=linker
            print(linker)
            print(linker, "_____________________")
            for i in range(maxprevlength, newlenght):
                print(i)
                checker(i)
            print(maxprevlength)
            print(newlenght)


# writer = pd.ExcelWriter('hotelsreview.xlsx')
# Frame.to_excel(writer, sheet_name='Sheet1', index='False')
# writer.save()
Frame.to_csv("review.csv",sep="\t")

WriteListofHotels(list_of_hotels)


# writer = pd.ExcelWriter('hotelsname.xlsx')
# hotellist.to_excel(writer, sheet_name='Sheet2', index='False')
# writer.save()
hotellist.to_csv("hotel.csv",sep="\t")
log=open("logs.txt",mode='w')
log.writelines(str(lastreviewlist))
log.writelines("\n")
log.writelines(str(filejsonlist))
log.close()
