import json

# Encoding from dictionaries and writing to JSON file
car_data = {"name": "tesla", "engine": "electric"}
print(car_data)
# printing the dictionary

print(type(car_data))
# checking the type of dictionary
# Prints <class 'dict'>


# print(car_data)

car_data_json_string = json.dumps(car_data)
# json.dumps changes python dict to json str
# The dumps() method translates simply python objects to JSON

print(type(car_data_json_string))

with open("new_json_file.json", "w") as jsonfile:
    # opening a new file called new_json_file.json, permission type write 'w'
    # jsonfile as the alias
    # Encoding and writing into json file

    json.dump(car_data, jsonfile)
    #json.dump takes 2 args
    # first argument is dictionary, second argument is file_type (jsonfile)

with open("new_json_file.json") as jsonfile:
    # Decoding
    # Reading the file we have created
    car = json.load(jsonfile)

    print(type(car))
    # checking the type of data again

    print(car['name']) # to get the value stored in the key called 'name'
    print(car['engine']) # to get the value of second key value pair

# We have decoded our file 'new_json_file.json'
# We have used dumps(), dump() and load() methods