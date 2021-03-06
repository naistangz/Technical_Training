import requests
import json

post_codes_requests = requests.get("https://api.postcodes.io/postcodes/EN40NB")

post_codes_requests_status = post_codes_requests.status_code


# Why should we use built in packages

# First iteration
if post_codes_requests.status_code == 200:
    print("Your request was successful")
elif post_codes_requests.status_code == 404:
    print("Sorry your request is not available")
elif post_codes_requests.status_code == 500:
    print("Server Error")

# Second iteration without comparison operators
def check_status_code():
    if post_codes_requests.status_code:
        print("Your request was successful")
    elif post_codes_requests.status_code:
        print("Sorry the page is not available")

check_status_code()

# Third iteration create same function with OOP - class and a method
# Create a method called check_status_code():
# Output should the same as we achieved without OOP.

class HTTPStatusCode:

    def check_status_code(self, request):
        if request:
            print(f"Your request was successful\nStatus Code: {request}")
        else:
            print("Sorry your request is not available")
            return


# print(post_codes_requests.headers)
# print(post_codes_requests.cookies)
# print(post_codes_requests.json())
# print(type(post_codes_requests))

c = HTTPStatusCode()
c.check_status_code(request=None) # Prints Sorry your request is not available
c.check_status_code(request=post_codes_requests_status) # Prints Your request was successful\nStatus Code: 200

json_data = post_codes_requests.json()
# storing data from json()
print(type(json_data)) # Prints <class 'dict'>



# Exercise is to fetch data by key value pairs within dictionaries
# Create a function to return the above values (key, value pairs)

# Iterating through keys. Without .key, it will iterate through keys by default
for key in json_data:
    print(key)
    # Prints status, result

print(json_data)

# Iterating through values
for value in json_data.values():
    print(value)

# Iterating through key, value pairs
class JSONIterator:
    def key_value_pair(self, json_dictionary):
        for k, v in json_dictionary.items():
            if type(v) is dict:
                self.key_value_pair(v)
            # kv = k, v
            else:
                print(k, ":", v)

json_test = JSONIterator()
json_test.key_value_pair(json_data)


