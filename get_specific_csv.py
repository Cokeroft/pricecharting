import requests
import datetime

from get_prices_csv import get_prices_from_csv
from compare import compare2


token = 'fca399e16c6c124270a7f737ce533a54ca9141ea'


def main():
    get_specific_csv()


def get_specific_csv():
    date = datetime.datetime.today()
    console = input("Which console do you want to search for? ")
    console_dash = console.replace(" ", "-").lower()
    compare_answer = input("Do you want to also compare the prices? ").lower()
    if compare_answer == "yes":
        compare_days = input("And how many days ago do you want to compare against? ")
        compare_days = int(compare_days)
        loose_price_list, cib_price_list, new_price_list, game_id_list = compare2(compare_days, console_dash)

    counter = 0

    #get_prices_from_csv(console)

    # Open the data file for the Console
    try:
        prices_file = open('prices/' + console_dash + '/prices_' + str(date.strftime('%m-%d-%Y')) + '.txt', 'r')
    except IOError:
        print("That file does not exist!")
        exit()
    contents = prices_file.readlines()

    print()

    for x in contents:
        if prices_file.mode == 'r':
            splitter = x.split("/")
            game_id = splitter[0].strip()
            name = splitter[1].replace(" ", "")
            loose_price = splitter[2].replace(" ", "")
            cib_price = splitter[3].replace(" ", "")
            new_price = splitter[4].replace(" ", "")
            # Check to see if we're missing data, in which case we skip. Otherwise it looks wonky!
            if loose_price == "" or cib_price == "" or new_price == "":
                print("The item '" + name + "' is missing some data!")
                print()
                counter += 1
                continue
            print("The item '" + name + "' is currently running " + str(loose_price) + " loose, "
                  + str(cib_price) + " complete, and " + str(new_price) + " brand new")
            #price_list.append(loose_price)
            #game_id_list.append(code)

            if compare_answer == "yes":
                if game_id_list[counter].strip() != game_id:
                    print("Oops, looks like the game ID doesn't match!")
                    counter += 1
                    continue

                difference_loose = float(loose_price.replace("$", "")) - float(loose_price_list[counter])
                difference_cib = float(cib_price.replace("$", "")) - float(cib_price_list[counter])
                difference_new = float(new_price.replace("$", "")) - float(new_price_list[counter])

                old_price_loose = loose_price_list[counter]
                old_price_cib = cib_price_list[counter]
                old_price_new = new_price_list[counter]

                percent_change_loose = get_change(float(loose_price.replace("$", "")), float(old_price_loose))
                percent_change_cib = get_change(float(cib_price.replace("$", "")), float(old_price_cib))
                percent_change_new = get_change(float(new_price.replace("$", "")), float(old_price_new))

                print("The old prices were: ")

                if difference_loose > 0 or difference_cib > 0 or difference_new > 0:
                    print("    Loose: $" + old_price_loose + " a total difference of $" + str(round(difference_loose, 2))
                          + " and a % increase of " + str(round(percent_change_loose, 2)) + "%!")
                elif difference_loose == 0:
                    print("    Loose: $" + old_price_loose +
                          " with no difference changes in total or percentage")
                elif difference_loose < 0:
                    print("    Loose: $" + old_price_loose + " a total difference of $" + str(round(difference_loose, 2))
                          + " and a % decrease of " + str(round(percent_change_loose, 2)) + "%!")

                if difference_cib > 0:
                    print("    Complete: $" + old_price_cib + " a total difference of $" + str(round(difference_cib, 2))
                          + " and a % increase of " + str(round(percent_change_cib, 2)) + "%!")
                elif difference_cib == 0:
                    print("    Complete: $" + old_price_cib +
                          " with no difference changes in total or percentage")
                elif difference_cib < 0:
                    print("    Complete: $" + old_price_cib + " a total difference of $" + str(round(difference_cib, 2))
                          + " and a % decrease of " + str(round(percent_change_cib, 2)) + "%!")

                if difference_new > 0:
                    print("    New: $" + old_price_new + " a total difference of $" + str(round(difference_new, 2))
                          + " and a % increase of " + str(round(percent_change_new, 2)) + "%!")
                elif difference_new == 0:
                    print("    New: $" + old_price_new +
                          " with no difference changes in total or percentage")
                elif difference_new < 0:
                    print("    New: $" + old_price_new + " a total difference of $" + str(round(difference_new, 2))
                          + " and a % decrease of " + str(round(percent_change_new, 2)) + "%!")

                print()

            else:
                print()

            #print(loose_price_list[counter], cib_price_list[counter], new_price_list[counter])
            counter += 1


def get_change(current, previous):
    if current == previous:
        return 100.0
    try:
        return (abs(current - previous) / previous) * 100.0
    except ZeroDivisionError:
        return 0


main()