import requests
import datetime

from get_data import get_data


token = 'fca399e16c6c124270a7f737ce533a54ca9141ea'


def main(console):
    get_prices_specific(console)


def get_prices_specific(console):
    date = datetime.datetime.today()
    console_dash = console.replace(" ", "-").lower()
    # Create Prices File to store the prices later
    prices_file = open('prices/' + console_dash + '/prices_' + str(date.strftime('%m-%d-%Y')) + '.txt', 'w')

    game_id_counter = get_data(console)
    # TODO - Need to add logic here to compare if the data is the same or not. If it is, get_data, if not, don't.
    counter = 0

    # Open the data file for Virtual Boy
    new_data_file = open('game_ids/' + console + '.txt', 'r+')
    contents = new_data_file.readlines()
    for x in contents:
        # Get the Game ID and strip it
        game_id = (x.replace("[", "").replace("'", "").replace("\n", "").lstrip())
        # Call the product API using the game_id
        # TODO - Make this async... somehow
        response = requests.get(f'https://www.pricecharting.com/api/product?t={token}&id={game_id}')
        # Set all the values I need
        loose_price = response.json()["loose-price"] * .01
        complete_price = response.json()["cib-price"] * .01
        new_price = response.json()["new-price"] * .01
        product_name = response.json()["product-name"]
        response_id = response.json()["id"]

        # Write to the Prices file
        prices_file.write(response_id + " / " + product_name + " / " + str(loose_price) + " / "
                          + str(complete_price) + " / " + str(new_price) + " / " + '\n')
        # When rounding from the prices file, always round. It doesn't want to round in there for me
        print("The item '" + product_name + "' is currently running $" + str(round(loose_price, 2)) + " loose, $"
              + str(round(complete_price, 2)) + " complete, and $" + str(round(new_price, 2)) + " brand new")

        counter += 1

    print("Priced " + str(game_id_counter) + " total items!")
    new_data_file.close()


def get_change(current, previous):
    if current == previous:
        return 100.0
    try:
        return (abs(current - previous) / previous) * 100.0
    except ZeroDivisionError:
        return 0

