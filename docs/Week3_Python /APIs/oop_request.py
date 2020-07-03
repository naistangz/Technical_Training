# Using OOP to perform a HTTP request
import requests

response_bbc = requests.get("https://www.bbc.co.uk")
print("The request code is: "+ str(response_bbc.status_code))

def check_response_code():
    if response_bbc.status_code == 200:
        print("Your request has been successful!")
    elif response_bbc.status_code == 400:
        print("The page you have requested has not been found")
    elif response_bbc.status_code == 404:
        print("Woops sorry the info you are looking for is not available")
    else:
        print("The error code could not be found")


check_response_code()

class Response:
    check_response_code()

Response()