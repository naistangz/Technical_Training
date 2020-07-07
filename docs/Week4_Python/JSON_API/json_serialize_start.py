# Process JSON data returned from a server

# use the JSON module
import json


def main():
    # define a python ditcionary
    pythonData = {
        "sandwich": "Reuben",
        "toasted": True,
        "toppings": ["Thousand Island Dressing",
                     "Sauerkraut",
                     "Pickles"
                     ],
        "price": 8.99
    }

    # TODO: serialize to JSON using dumps
    jsonStr = json.dumps(pythonData, indent=4)
    # Printed all on one line which is fixed using the indent parameter of the Dump S function
    # Above indents each level by four spaces

    # TODO: print the resulting JSON string
    print("JSON Data: --------")
    print(jsonStr)


# if __name__ == "__main__":
#     main()

if __name__ == "__main__":
    print("This program is being run by itself")
else:
    print("I am being imported from another module")