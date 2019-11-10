import datetime

token = 'fca399e16c6c124270a7f737ce533a54ca9141ea'


def compare(offset):
    date = datetime.datetime.today() - datetime.timedelta(offset)

    try:
        f = open('prices/virtual-boy/prices_' + str(date.strftime('%m-%d-%Y')) + '.txt', 'r')
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
