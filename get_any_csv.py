import datetime

from get_prices_csv import get_prices_from_csv
from compare import compare2


token = 'fca399e16c6c124270a7f737ce533a54ca9141ea'


def main():
    get_any_csv()


def get_any_csv():
    date = datetime.datetime.today()
    console = input("Which console do you want to search for? ")
    console_dash = console.replace(" ", "-").lower()
    compare_answer = input("Do you want to also compare the prices? ").lower()
    if compare_answer == "yes":
        compare_days_str = input("And how many days ago do you want to compare against? ")
        compare_days = int(compare_days_str)
        try:
            loose_price_list, cib_price_list, new_price_list, game_id_list, name_list = compare2(compare_days, console_dash)
        except IOError:
            print("That data does not exist, try another date!")
            exit()

    get_prices_from_csv(console)
    # Set all the values before we get into the for loop
    counter = 0
    difference_gain_loose = 0
    difference_gain_cib = 0
    difference_gain_new = 0

    # Open the data file for the Console
    try:
        prices_file = open('prices/' + console_dash + '/prices_' + str(date.strftime('%m-%d-%Y')) + '.txt', 'r')
    except IOError:
        print("That file does not exist!")
        exit()
    contents = prices_file.readlines()

    print()
    active_game_id_list = []

    for x in contents:
        if prices_file.mode == 'r':
            # Read the data file that we just created
            splitter = x.split("//")
            game_id = splitter[0].strip()
            name = splitter[1].strip()
            active_game_id_list.append(game_id)
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

            # Run the compare function if the user wants to
            if compare_answer == "yes":
                try:
                    if game_id_list[counter].strip() != game_id:
                        new_active_game_id_list = active_game_id_list
                        if game_id_list[counter].strip() in new_active_game_id_list:
                            # This will fix the list and also report the misplaced item.
                            print("That ID already was used, looks like it got renamed!")
                            print("But here is our best attempt to getting the prices anyways")
                            print()
                            compare_next(loose_price, loose_price_list, cib_price, cib_price_list, new_price,
                                         new_price_list, counter+1)
                            counter += 2
                            continue
                        print("Oops, looks like the game ID doesn't match!")
                        print()
                        continue
                except IndexError:
                    print("Oops you've hit the end of the file, RIP!")
                    exit()

                if loose_price_list[counter] == "" or cib_price_list[counter] == "" or new_price_list[counter] == "":
                    print("The item '" + name + "' is missing some compare data!")
                    print()
                    counter += 1
                    continue

                # I can probably get the below all into a single method, but that would require a lot of passing
                # of variables. I think for now I'll leave it as is, even though it's bulky.

                difference_loose = float(loose_price.replace("$", "")) - float(loose_price_list[counter])
                difference_cib = float(cib_price.replace("$", "")) - float(cib_price_list[counter])
                difference_new = float(new_price.replace("$", "")) - float(new_price_list[counter])

                old_price_loose = loose_price_list[counter]
                old_price_cib = cib_price_list[counter]
                old_price_new = new_price_list[counter]

                percent_change_loose = get_change(float(loose_price.replace("$", "")), float(old_price_loose))
                percent_change_cib = get_change(float(cib_price.replace("$", "")), float(old_price_cib))
                percent_change_new = get_change(float(new_price.replace("$", "")), float(old_price_new))

                if percent_change_loose > difference_gain_loose:
                    difference_gain_loose = percent_change_loose
                    difference_gain_loose_value = loose_price
                    difference_name_loose = name

                if percent_change_cib > difference_gain_cib:
                    difference_gain_cib = percent_change_cib
                    difference_gain_cib_value = cib_price
                    difference_name_cib = name

                if percent_change_new > difference_gain_new:
                    difference_gain_new = percent_change_new
                    difference_gain_new_value = new_price
                    difference_name_new = name

                print("The old prices were: ")

                if difference_loose > 0:
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

            counter += 1

    if compare_answer == "yes":
        print_gainers(difference_gain_loose, difference_gain_cib, difference_gain_new, compare_days_str,
                      difference_name_loose, difference_gain_loose_value, difference_name_cib,
                      difference_gain_cib_value, difference_name_new, difference_gain_new_value)


def print_gainers(difference_gain_loose, difference_gain_cib, difference_gain_new, compare_days_str,
                  difference_name_loose, difference_gain_loose_value, difference_name_cib,
                  difference_gain_cib_value, difference_name_new, difference_gain_new_value):
    # Am I ever going to even reuse this? Does it even need a method? The world may never know
    if difference_gain_loose > 0:
        print("The biggest loose gainer in value was " + difference_name_loose + " which increased by a whopping " +
              str(round(difference_gain_loose, 2)) + "%! You should've bought it " +
              compare_days_str + " days ago! Current Price: " + difference_gain_loose_value)
    else:
        print("No games gained value in loose!")

    if difference_gain_cib > 0:
        print("The biggest complete gainer in value was " + difference_name_cib + " which increased by a whopping "
              + str(round(difference_gain_cib, 2)) + "%! You should've bought it " +
              compare_days_str + " days ago! Current Price: " + difference_gain_cib_value)
    else:
        print("No games gained value in complete!")

    if difference_gain_new > 0:
        print("The biggest new gainer in value was " + difference_name_new + " which increased by a whopping " +
              str(round(difference_gain_new)) + "%! You should've bought it " +
              compare_days_str + " days ago! Current Price: " + difference_gain_new_value)
    else:
        print("No games gained value in new!")


def get_change(current, previous):
    if current == previous:
        return 0
    try:
        return (abs(current - previous) / previous) * 100.0
    except ZeroDivisionError:
        return 0


def compare_next(loose_price, loose_price_list, cib_price, cib_price_list, new_price, new_price_list, counter):
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

    if difference_loose > 0:
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


main()
