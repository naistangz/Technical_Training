import requests
import json

post_codes_requests = requests.get("https://api.postcodes.io/postcodes/se120nb")

print(post_codes_requests.status_code)
# why should we use built in packages

if post_codes_requests.status_code == 200:
    print("Your request was successful")
elif post_codes_requests.status_code == 400:
    print("Sorry your request is not available")
