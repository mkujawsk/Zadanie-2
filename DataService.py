from re import T

import requests

import matplotlib.pyplot as plt

class DataService:
    @staticmethod
    def get_list_holidays(year):

        #
        tabresult=[]
        result = requests.get(f"https://date.nager.at/api/v3/PublicHolidays/{year}/PL").json()

        for x in result:
            tabresult.append(x['localName'])        
        tabresult.sort()

        return tabresult

    @staticmethod
    def draw_graph(YearLow, YearHigh,ChosenHoliday):
        


        #calendar days
        x_datestab =[]
        while YearLow <= YearHigh:
            result = requests.get(f"https://date.nager.at/api/v3/PublicHolidays/{YearLow}/PL").json()
            
            Name4Date = dict()
            for item in result:
                name = item['localName']
                date = item['date']
                Name4Date[name] = date

            x_datestab.append(Name4Date[ChosenHoliday])
            YearLow = YearLow + 1

        print (x_datestab)


        #average daily temp
        y_tempstab = []
        for item in x_datestab:
            year = item[:4]
            month = item[5:7]
            day = item[8:10]

            result = requests.get(f"https://www.metaweather.com/api/location/523920/{year}/{month}/{day}").json()

            #multiple entries per day - calculate average
            counter = 1
            avg_temp = 0
            for item2 in result:
                temp = item2['the_temp']

                #skip empty
                if(temp != None): 
                    avg_temp = avg_temp + temp
                    counter = counter + 1

            #average
            avg_temp = avg_temp/counter
            y_tempstab.append(avg_temp)

        
        #create plot
        dev_x = x_datestab
        dev_y = y_tempstab

        plt.plot(dev_x,dev_y)
        plt.xticks(rotation=90)
        plt.show()

        return