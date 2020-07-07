# Process JSON data returned from a server

# TODO: use the JSON module
# Importing the JSON module
import json

def main():
    # define a string of JSON code
    jsonStr = '''{
            "sandwich" : "Reuben",
            "toasted" : true,
            "toppings" : [
                "Thousand Island Dressing",
                "Sauerkraut",
                "Pickles"
            ],
            "price" : 8.99
        }'''

    # TODO: parse the JSON data using loads
    # This will build a native python dictionary for me.
    # Once I have that object, I can work with like any other Python dictionary
    data = json.loads(jsonStr)

    # TODO: print information from the data structure
    # Here the key name is sandwich
    print("Sandwich: "+ data['sandwich']) # indexing it by the key name
    if (data['toasted']):
        print("And it's toasted!")
    for topping in data['toppings']:
        print("Topping: " + topping)



# Whenever the Python interpreter reads a source file, it does two things:
# Sets a few special variables like __name__, and then
# Executes all of the code found in the file
# The interpreter will assign hard-coded string "__main__" to the "__name__" variable
if __name__ == "__main__":
    print("This program is being run by itself")
else:
    print("I am being imported from another module")
