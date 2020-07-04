import requests

# Check HTTP/HTTPs
# 200 success
# 400 404 page not found

# Making a get request
# Check that b' is at the start of output, which references to a bytes object
response_bcc = requests.get("https://www.bbc.co.uk/")

# Returns <Response [200]>
print(response_bcc)

print(response_bcc.status_code)

print(response_bcc.headers)

# Returns <class 'requests.structures.CastInsensitiveDict'>
print(type(response_bcc.headers))

# .content gives access to the raw bytes of the response payload
# Print request content
print(response_bcc.content)
