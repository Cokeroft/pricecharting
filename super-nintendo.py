import requests
import datetime


token = 'fca399e16c6c124270a7f737ce533a54ca9141ea'


def main():
    # token = get_token()
    #get_super_nintendo_all()
    get_tree_d_o_all()


def get_super_nintendo_all():
    date = datetime.datetime.today()
    my_data_file = open('prices_' + str(date.strftime('%m-%d-%Y')) + '.txt', 'w')
    snes_games = ["6842", "6858", "6910", "12576"]
    print(f'found {len(snes_games)} games to check')

    counter = 0
    for i in snes_games:
        response = requests.get(f'https://www.pricecharting.com/api/product?t={token}&id={i}')
        loose_price = response.json()["loose-price"] * .01
        product_name = response.json()["product-name"]
        my_data_file.write(i + " / " + product_name + " / " + str(loose_price) + " / " + '\n')

        f = open('prices_09-28-2019.txt', 'r')
        contents = f.readlines()
        price_list = []
        for x in contents:
            if f.mode == 'r':
                splitter = x.split("/")
                code = splitter[0]
                name = splitter[1]
                price = splitter[2]
                price_list.append(price)
        print(product_name + ' is currently going for $' + str(loose_price))
        difference = float(loose_price) - float(price_list[counter])
        print("and the old price was $" + price_list[counter] + " a total difference of $" + str(round(difference, 2)))
        counter += 1

    my_data_file.close()


def get_tree_d_o_all():
    date = datetime.datetime.today()
    my_data_file = open('3doprices_' + str(date.strftime('%m-%d-%Y')) + '.txt', 'w')
    tree_do_o_games = open('3DO.txt', 'r')
    contents = tree_do_o_games.read()
    # print(f'found {len(snes_games)} games to check')

    counter = 0
    for i in tree_do_o_games:
        for x in contents:
            game_id = x.replace("[", "").replace("'", "").lstrip()
            print(game_id)
            response = requests.get(f'https://www.pricecharting.com/api/product?t={token}&id={game_id}')
            loose_price = response.json()["loose-price"] * .01
            product_name = response.json()["product-name"]
        my_data_file.write(i + " / " + product_name + " / " + str(loose_price) + " / " + '\n')

        f = open('prices_09-28-2019.txt', 'r')
        contents = f.readlines()
        price_list = []
        for x in contents:
            if f.mode == 'r':
                splitter = x.split("/")
                code = splitter[0]
                name = splitter[1]
                price = splitter[2]
                price_list.append(price)
        print(product_name + ' is currently going for $' + str(loose_price))
        difference = float(loose_price) - float(price_list[counter])
        print("and the old price was $" + price_list[counter] + " a total difference of $" + str(round(difference, 2)))
        counter += 1

    my_data_file.close()

def read_data():
    f = open('prices_09-28-2019.txt', 'r')
    contents = f.readlines()
    d = dict()

    for i in contents:
        if f.mode == 'r':
            splitter = i.split("/")
            price = splitter[2]
            d[i] = price

    return d


'''
todo list
1. break into multiple functions -- DONE
2. read files from selection, maybe ask which file they want to compare to and do that -- DONE
3. add more details to prints, such as "a % increase/decrease!" -- DONE
4. add logic around negative/positive, so it says increase or decrease of -- DONE
5. If it's negative, put the $ after the negative sign. ie: -$7 instead of $-7

long term:
find solution for getting all IDs back. maybe read from the csv -- DONE see get_data.py
https://www.pricecharting.com/price-guide/download-custom?t=fca399e16c6c124270a7f737ce533a54ca9141ea is the URL
find a way to parse that so you can only search the super nintendo IDs, etc. maybe write those a file before you use it?'''

main()
