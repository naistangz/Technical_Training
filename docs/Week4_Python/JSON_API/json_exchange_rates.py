# Task
# import JSON
# create a class called Exchange_Rates with required attributes
# fetch the data from exchange_rates.json
# display the data
# display the type of the data
# display exchange rates with specific currencies

import json

class Exchange_Rates:
    def __init__(self):
        with open("exchange_rates.json", "r") as exchange_files: # name aliasing
            data = json.load(exchange_files)
            for i in data:
                if i == 'base':
                    print(data['base']) # Prints value of base: 'EUR'
            print(data)

    def fetch_exchange_rates(self):
        with open("exchange_rates.json", "r") as jsonfile:
            currencies = json.load(jsonfile)
            # For loop to get all exchange rates
            while True:
                for key in currencies:
                    if key == "rates":
                        print(currencies["rates"])
                        currency = input("Select currency to exchange with EUR as base currency: \n").upper()
            # Display exchange rates with specific currency
                        print(f"1 Euro: " + str(currencies["rates"][currency]))





e = Exchange_Rates
print(e)
e.__init__(Exchange_Rates)
e.fetch_exchange_rates(Exchange_Rates)



