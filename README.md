# Pricecharting Scripts

These are some scripts to help compare prices, not much atm


## Get Any From CSV

```bash
./get_any_csv.py
```

You can enter most consoles, but they must be entered correctly. 
For example Virtual Boy or Super Nintendo or NES.
 
 You will then be prompted if you want to compare with older prices. You can say Yes or No
 
 ## Get Prices
 
 ```bash
 ./get_prices_all.py
 ```
 
 This will create the prices file for the current day for all games from Nintendo, Sony, Sega, 
 Microsoft, and other misc items such as Amiibo and Nintendo Power.
 
  ## Search
 
 ```bash
 ./search.py
 ```
 
 This will let you search for the products you want to search for, return the results in
 option format and will then let you pick which one to further search for. Let's you narrow
 down the results a bit if there are a lot!
 
 TODO - Going to add functionality to let you find the ID in the prices file and compare!
 
 ## DEPRECATED BELOW
 
 ## Get Data
 ```bash
 ./get_data.py
 ```
 
 This will get the data IDs used for API searching for a specific console. In the future,
 I'll update this to be able to find a specific ID based off console.
