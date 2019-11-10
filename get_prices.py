import requests

token = 'fca399e16c6c124270a7f737ce533a54ca9141ea'


def get_prices(prices_file, contents):
    game_id_list = []
    loose_price_list = []
    for x in contents:
        # Get the Game ID and strip it
        game_id = (x.replace("[", "").replace("'", "").replace("\n", "").lstrip())
        game_id_list.append(game_id)
        # Call the product API using the game_id
        response = requests.get(f'https://www.pricecharting.com/api/product?t={token}&id={game_id}')
        # Set all the values I need
        loose_price = response.json()["loose-price"] * .01
        loose_price_list.append(loose_price)
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

    return game_id_list, loose_price_list
