import requests
import json

post_codes_requests = requests.get("https://api.postcodes.io/postcodes/se120nb")

print(post_codes_requests.status_code)
# Why should we use built in packages

# First iteration
# if post_codes_requests.status_code == 200:
#     print("Your request was successful")
# elif post_codes_requests.status_code == 404:
#     print("Sorry your request is not available")
# elif post_codes_requests.status_code == 500:
#     print("Server Error")

# Second iteration without comparison operators
# def check_status_code():
#     if post_codes_requests.status_code:
#         print("Your request was successful")
#     elif post_codes_requests.status_code:
#         print("Sorry the page is not available")
#
# check_status_code()

# Third iteration create same function with OOP - class and a method
class HTTPStatusCode:
    response = None

    def check_status_code(self, response):
        if response is not None:
            self.response = response.status_code
        else:
            print("Sorry your request is not available")

c = HTTPStatusCode()
# c.check_status_code(HTTPStatusCode)