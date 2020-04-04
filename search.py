import requests
import datetime


token = 'fca399e16c6c124270a7f737ce533a54ca9141ea'


def main():
    search()


def search():
    date = datetime.datetime.today()
    query = input("What do you want to search for? ")

    # Add logic to search, and provide the results to the user.
    response = requests.get(f"https://www.pricecharting.com/api/products?t={token}&q={query}")
    response_length = len(response.json()["products"])
    option_dict = dict()
    print()
    for i in range(response_length):
        # Print out the results and save the game id to the dict
        # Can I do anything more here, save anything else? TODO
        print("Option #" + str(i + 1) + ": ")
        print("----------------------------------------------------")
        print("Game Name: " + response.json()["products"][i]["product-name"])
        print("Console: " + response.json()["products"][i]["console-name"] + "\n")

        option_dict[i + 1] = response.json()["products"][i]["id"]

    # Select which one you want to get more details on
    option = input("Which option do you want more details on? (Just enter the number) ")

    response = requests.get(f"https://www.pricecharting.com/api/product?t={token}&id={option_dict[int(option)]}")
    print_results(response)

    # Start the Compare stuff
    compare_answer = input("Do you want to compare the current price for this game? ").lower()
    if compare_answer == "yes":
        print("Yes compare")
        # Add logic here to search the folders of data and compare the specific game. Lots of parsing I guess


def print_results(response):
    loose_price = response.json()["loose-price"] * .01
    complete_price = response.json()["cib-price"] * .01
    new_price = response.json()["new-price"] * .01
    print("\n" + response.json()["product-name"])
    print(response.json()["console-name"])
    print("Loose Price: $" + str(loose_price))
    print("CIB Price: $" + str(complete_price))
    print("New Price: $" + str(new_price))
    print()


main()
