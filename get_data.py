import requests
import csv

token = 'fca399e16c6c124270a7f737ce533a54ca9141ea'


def get_data(console):
    url = 'https://www.pricecharting.com/price-guide/download-custom?t=fca399e16c6c124270a7f737ce533a54ca9141ea'

    with requests.Session() as s:
        download = s.get(url, timeout=25)

        decoded_content = download.content.decode('utf-8')

        # This is reading the file, and converting to a list
        # Also, using quotechar to block the case where a comma is in the game title
        cr = csv.reader(decoded_content.splitlines(), delimiter=',', quotechar="'", quoting=csv.QUOTE_MINIMAL)
        my_list = list(cr)

        # Counters for increasing
        counters = 0
        game_id_counter = 0

        # Full list of the console games, or whatever you search for
        proper_list = [x for x in my_list if console in x]
        if len(proper_list) == 0:
            print("What did you do? That console doesn't exist")
            exit()

        # Splitting them up instead single strings so I can save to a file
        counter = str([x for x in my_list if console in x]).split(",")

        my_data_file = open('game_ids/' + console + '.txt', 'w')
        # Writing to the 3DO file
        for i in proper_list:
            length = len(i)
            game_id = counter[counters]
            my_data_file.write(game_id + "\n")
            print("Added Game ID " + counter[counters] + "]")
            # Increasing by the length, so it adds up correctly
            counters += length
            game_id_counter += 1

        my_data_file.close()

        print("Added " + str(game_id_counter) + " games and/or products!")

        return game_id_counter
