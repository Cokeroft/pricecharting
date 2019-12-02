import datetime

import requests
import csv

token = 'fca399e16c6c124270a7f737ce533a54ca9141ea'


def get_prices_from_csv(console):
    url = 'https://www.pricecharting.com/price-guide/download-custom?t=fca399e16c6c124270a7f737ce533a54ca9141ea'

    with requests.Session() as s:
        date = datetime.datetime.today()
        download = s.get(url, timeout=25)

        decoded_content = download.content.decode('ISO-8859-1')

        # This is reading the file, and converting to a list
        # Also, using quotechar to block the case where a comma is in the game title
        cr = csv.reader(decoded_content.splitlines(), delimiter=',', quotechar="'", quoting=csv.QUOTE_MINIMAL)
        my_list = list(cr)

        # Counters for increasing
        counters = 0
        name_counters = 2
        loose_price_counters = 3
        complete_price_counters = 4
        new_price_counters = 5
        game_id_counter = 0

        # Full list of the console games, or whatever you search for
        proper_list = [x for x in my_list if console in x]
        if len(proper_list) == 0:
            print("What did you do? That console doesn't exist")
            exit()

        # Splitting them up instead single strings so I can save to a file
        counter = str([x for x in my_list if console in x]).split(",")

        console_dash = console.replace(" ", "-").lower()
        prices_file = open('prices/' + console_dash + '/prices_' + str(date.strftime('%m-%d-%Y')) + '.txt', 'w')
        # Writing to the file
        for i in proper_list:
            length = len(i)
            # TODO - Got to be a better way to do this! The finding of the data I want that is
            game_id = counter[counters].replace("[", "").replace("'", "").replace(" ", "")
            product_name = counter[name_counters].replace("'", "")
            loose_price = counter[loose_price_counters].replace("'", "")
            complete_price = counter[complete_price_counters].replace("'", "")
            new_price = counter[new_price_counters].replace("'", "")
            prices_file.write(game_id + " / " + product_name + " / " + str(loose_price) + " / " + str(complete_price)
                               + " / " + str(new_price) + " / " + "\n")

            # This print is not needed, but will keep for debugging
            # print("Added Game ID " + counter[counters] + "]")
            # Increasing by the length, so it adds up correctly
            counters += length
            name_counters += length
            loose_price_counters += length
            complete_price_counters += length
            new_price_counters += length
            game_id_counter += 1

        prices_file.close()

        print("Added " + str(game_id_counter) + " games and/or products!")
