import xlrd
import csv
from bs4 import BeautifulSoup

def csv_from_excel():

    wb = xlrd.open_workbook('hotelsname.xlsx')
    sh = wb.sheet_by_name('Sheet2')
    csv = open('hotels.csv', 'w')


    csv.write('id,price,street-address,locality,region,name,imgurl\n');


    for rownum in range(1,sh.nrows):
        data = ""
        for colnum in range (sh.ncols):
            if(colnum == 2):
                soup = BeautifulSoup(sh.col_values(colnum, start_rowx=rownum)[0], 'xml')
                street_address = soup.find_all("span", class_="street-address")
                locality = soup.find_all("span", property="v:locality")
                region = soup.find_all("span", property="v:region")
                address = ""
                for classnode in street_address:
                    address += str(classnode.string)
                address += ','

                for classnode in locality:
                    address += str(classnode.string)
                address += ','

                for classnode in region:
                    address += str(classnode.string)

                print(address)

                data += address+','
            else:
                data += sh.col_values(colnum, start_rowx=rownum)[0]
                if colnum < sh.ncols-1:
                    data += ','
                else:
                    data += '\n'
        # print(data)
        csv.write(data)



    csv.close()

csv_from_excel()
