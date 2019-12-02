import datetime

token = 'fca399e16c6c124270a7f737ce533a54ca9141ea'


def compare(offset, console):
    date = datetime.datetime.today() - datetime.timedelta(offset)

    try:
        f = open('prices/' + console + '/prices_' + str(date.strftime('%m-%d-%Y')) + '.txt', 'r')
    except IOError:
        print("That file does not exist!")
    contents = f.readlines()
    price_list = []
    game_id_list = []
    for x in contents:
        if f.mode == 'r':
            splitter = x.split("/")
            code = splitter[0]
            name = splitter[1]
            loose_price = splitter[2]
            cib_price = splitter[3]
            new_price = splitter[4]
            price_list.append(loose_price)
            game_id_list.append(code)
    return price_list, game_id_list


def compare2(offset, console):
    date = datetime.datetime.today() - datetime.timedelta(offset)

    try:
        f = open('prices/' + console + '/prices_' + str(date.strftime('%m-%d-%Y')) + '.txt', 'r')
    except IOError:
        print("That file does not exist!")
        exit()
    contents = f.readlines()
    loose_price_list = []
    cib_price_list = []
    new_price_list = []
    game_id_list = []
    for x in contents:
        if f.mode == 'r':
            splitter = x.split("/")
            code = splitter[0].strip()
            name = splitter[1]
            loose_price = splitter[2].replace("$", "").strip()
            cib_price = splitter[3].replace("$", "").strip()
            new_price = splitter[4].replace("$", "").strip()
            loose_price_list.append(loose_price)
            cib_price_list.append(cib_price)
            new_price_list.append(new_price)
            game_id_list.append(code)
    return loose_price_list, cib_price_list, new_price_list, game_id_list

#def compare_message(loose_price, cib_price, new_price):
    #TODO - I'd like to take what is currently in get_specific_csv into here, so that I can take the numbers and
    # do all the messaging here. Look into it someday
