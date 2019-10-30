import requests
import datetime

from get_data import get_data

token = 'fca399e16c6c124270a7f737ce533a54ca9141ea'


def main():
    get_3do_all()


def get_3do_all():
    date = datetime.datetime.today()
    # Create Prices File to store the prices later
    prices_file = open('prices/3do/prices_' + str(date.strftime('%m-%d-%Y')) + '.txt', 'w')

    game_id_counter = get_data("3DO")

    # Open the data file for 3DO
    new_data_file = open('game_ids/3DO.txt', 'r+')
    contents = new_data_file.readlines()
    for x in contents:
        # Get the Game ID and strip it
        game_id = (x.replace("[", "").replace("'", "").replace("\n", "").lstrip())
        # Call the product API using the game_id
        response = requests.get(f'https://www.pricecharting.com/api/product?t={token}&id={game_id}')
        loose_price = response.json()["loose-price"] * .01
        product_name = response.json()["product-name"]
        id = response.json()["id"]
        prices_file.write(id + " / " + product_name + " / " + str(loose_price) + " / " + '\n')
        # When rounding from the prices file, always round. It doesn't want to round in there for me
        print("The item '" + product_name + "' is currently running $" + str(round(loose_price, 2)))

    print("Priced " + str(game_id_counter) + " total items!")
    new_data_file.close()


main()
