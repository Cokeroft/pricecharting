import sys
import requests
import datetime

from get_data import get_data
from compare import compare

token = 'fca399e16c6c124270a7f737ce533a54ca9141ea'


def main():
    get_any()


def get_any():
    date = datetime.datetime.today()
    console = input("Which console do you want to search for? ")
    console_dash = console.replace(" ", "-").lower()
    compare_answer = input("Do you want to also compare the prices? ").lower()
    if compare_answer == "yes":
        compare_days = input("And how many days ago do you want to compare against? ")
        compare_days = int(compare_days)
    # Create Prices File to store the prices later
    prices_file = open('prices/' + console_dash + '/prices_' + str(date.strftime('%m-%d-%Y')) + '.txt', 'w')

    game_id_counter = get_data(console)
    # Need to add logic here to compare if the data is the same or not. If it is, get_data, if not, don't.
    counter = 0

    # Open the data file for Virtual Boy
    new_data_file = open('game_ids/' + console + '.txt', 'r+')
    contents = new_data_file.readlines()
    for x in contents:
        # Get the Game ID and strip it
        game_id = (x.replace("[", "").replace("'", "").replace("\n", "").lstrip())
        # Call the product API using the game_id
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

        # Testing Offset Price Check
        if compare_answer == "yes":
            price_list, game_id_list = compare(compare_days)
            if game_id_list[counter].strip(" ") != game_id:
                print("Oops, looks like the game ID doesn't match!")
                # IT WORKS
                # TODO - Does this work? How should I handle this? Maybe a try/catch?
            difference = float(loose_price) - float(price_list[counter])
            old_price = float(price_list[counter])
            # Get the percent change
            percent_change = get_change(loose_price, old_price)
            # Logic paths for how the item has changed
        
            if difference > 0:
                print("and the old price was $" + str(round(old_price, 2)) + " a total difference of $"
                      + str(round(difference, 2)) + " and a % increase of " + str(round(percent_change, 2)) + "%!")
                print()
            elif difference == 0:
                print("and the old price was $" + str(round(old_price, 2)) +
                      " with no difference changes in total or percentage")
                print()
            elif difference < 0:
                print("and the old price was $" + str(round(old_price, 2)) + " a total difference of $"
                      + str(round(difference, 2)) + " and a % decrease of " + str(round(percent_change, 2)) + "%!")
                print()

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


main()
