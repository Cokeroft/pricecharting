import requests
import csv

token = 'fca399e16c6c124270a7f737ce533a54ca9141ea'


def get_data(console):
    url = 'https://www.pricecharting.com/price-guide/download-custom?t=fca399e16c6c124270a7f737ce533a54ca9141ea'

    with requests.Session() as s:
        download = s.get(url, timeout=25)

        decoded_content = download.content.decode('utf-8')

        # This is reading the file, and converting to a list
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
        new_list = []

        # print(new_list)
        # Random counters, probably not needed?
        counters = 0
        game_id_counter = 0

        #console = input("Which game console or poducts do you want to get data for? ")
        # Full list of the 3DO games, or whatever you search for
        proper_list = [x for x in my_list if console in x]
        if len(proper_list) == 0:
            print("What did you do? That console doesn't exist")
            exit()
        # Splitting them up instead single strings so I can save to a file
        counter = str([x for x in my_list if console in x]).split(",")
        # print(counter[0])
        my_data_file = open('game_ids/' + console + '.txt', 'w')
        # Writing to the 3DO file
        for i in proper_list:
            game_id = counter[counters]
            my_data_file.write(game_id + "\n")
            print("Added Game ID " + counter[counters] + "]")
            # 12 columns, so need to add by 12
            counters += 12
            game_id_counter += 1
        my_data_file.close()
        print("Added " + str(game_id_counter) + " games and/or products!")
        return game_id_counter
