import requests

# Iteration 1
# receive a response and check if 200 - print success
# elif code 400 - page not found
# else code 404 woops sorry the info you are looking for is not available
response_bbc = requests.get("https://www.bbc.co.uk/")
print(response_bbc)
if response_bbc.status_code == 200:
    print("Your request has been successful")
elif response_bbc.status_code == 400:
    print("The page you have requested has not been found")
elif response_bbc.status_code == 404:
    print("Woops sorry the info you are looking for is not available")


checking_response_code = response_bbc.status_code
print("The status code is : {}".format(str(checking_response_code)))


# Iteration 2
# Create a function called check_response_code() including all the above
# Returns the message with status code
response_bcc = requests.get("https://www.bbc.co.uk/")

def check_response_code():
    if response_bcc.status_code == 200:
        print("Your request has been successful")
    elif response_bcc.status_code == 400:
        print("The page you have requested has not been found")
    elif response_bcc.status_code == 404:
        print("Woops sorry the info you are looking for is not available")
    else:
        print("The error code could not be found")


# Iteration 3 Using OOP with 4 pillars
# Open file in import_request.py
class Response:
    check_response_code()

Response()