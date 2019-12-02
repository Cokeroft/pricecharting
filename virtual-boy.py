import requests
import datetime

from get_data import get_data
from compare import compare

token = 'fca399e16c6c124270a7f737ce533a54ca9141ea'


def main():
    get_vb_all()


def get_vb_all():
    date = datetime.datetime.today()
    # Create Prices File to store the prices later
    prices_file = open('prices/virtual-boy/prices_' + str(date.strftime('%m-%d-%Y')) + '.txt', 'w')

    game_id_counter = get_data("Virtual Boy")
    counter = 0

    # Open the data file for Virtual Boy
    new_data_file = open('game_ids/Virtual Boy.txt', 'r+')
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
        id = response.json()["id"]

        # Write to the Prices file
        prices_file.write(id + " / " + product_name + " / " + str(loose_price) + " / "
              + str(complete_price) + " / " + str(new_price) + " / " + '\n')
        # When rounding from the prices file, always round. It doesn't want to round in there for me
        print("The item '" + product_name + "' is currently running $" + str(round(loose_price, 2)) + " loose, $"
              + str(round(complete_price, 2)) + " complete, and $" + str(round(new_price, 2)) + " brand new")

        # Testing Offset Price Check
        price_list = compare(-30)
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

''' TODO LIST
1. Investigate the case where a game is removed from the CSV when comparing. Anyway to do a diff? Maybe some if logic
    around this case, where if the game IDs don't match up just skip? Probably easiest
2. Add logic around the compare, if that date doesn't exist it needs to fail gently
3. Add some async goodness to the API call. One at a time is not great for bigger consoles
4. Create a utility/helpers file, and throw get_change and stuff in there
5. Maybe investigate a way to avoid having to create a .py file for each console. Or maybe that is a good thing?
    Do we really need the ability to do all of em at once? Might be best to be able to target
    
    
Change this entire thing to be 1 function that asks what you want to check into, and then checks if that is valid

'''