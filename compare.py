import requests
import csv
import datetime

token = 'fca399e16c6c124270a7f737ce533a54ca9141ea'


def compare(offset):
    date = datetime.datetime.today() + datetime.timedelta(offset)
    # print(date.strftime('%m-%d-%Y'))

    f = open('prices/virtual-boy/prices_' + str(date.strftime('%m-%d-%Y')) + '.txt', 'r')
    contents = f.readlines()
    price_list = []
    counter = 0
    for x in contents:
        if f.mode == 'r':
            splitter = x.split("/")
            code = splitter[0]
            name = splitter[1]
            loose_price = splitter[2]
            cib_price = splitter[3]
            new_price = splitter[4]
            # Only can append one. Maybe create a function for all 3? Loose, Complete, New? Just need to set 3 variables then
            price_list.append(loose_price)
    # print(price_list[12])
    return price_list
