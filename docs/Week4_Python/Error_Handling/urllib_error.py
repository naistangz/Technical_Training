# Handling error and status codes

# Defines functions and classes to help open URLs (mostly HTTP)
import urllib.request

# Python module for fetching URLs using a variety of protocols
# HTTPError is subclass of URLError
# HTTPError Errors include 404 (page not found), 403 (request forbidden), and 401 (authentication required)
# HTTPError instance raised will have an integer code attribute, which corresponds to the error sent by the server
# URLError is raised when there is no network connection or the specified server does not exist
from urllib.error import HTTPError, URLError

# New in python 3.5, defines set of HTTP status codes, reason phrases and long descriptions
from http import HTTPStatus


class HTTP_Check():

    def __init__(self, url=None):
        self.url = url

    def main(self):

        # using exception handling when accessing URL
        # try URL and print HTTP status code
        try:
            response = urllib.request.urlopen(url)
            print(f"Response code:{response.status}")
            if (response.getcode() == HTTPStatus.OK): # or Status code == 200
                response_read = response.read()
                print(f"Hurrrah your request was successful\n{response_read}")
            f = open("successfulHTTP.txt", "w+")
            f.write(f"Wooop the HTTP request was successful\nResponse Code:{response.status}\n{response_read}")

        # exception when server returns an unsuccessful error code
        except HTTPError as e:
            f = open("errorHTTPlog.txt", "w+")
            f.write(f"Something exceptional just happened.\n{e}")
            f.close()
            print("Errrrrm your request could not be found")

        # When something is wrong with the URL itself i.e server does not exist. Reason method provides description.
        except URLError as e:
            f = open("errorlog.txt", "w+")
            f.write(f"Something exceptional just happened.\nHere is the error:{e.reason}")
            f.close()
            print("Hmmmmm something is wrong with the URL")



# # will generate a URLError
url = "http://no-such-server.org"

# will generate a HTTPError
# url = "http://httpbin.org/status/404"

# Successful request
# url = "http://httpbin.org/html"

# Instantiating class
h = HTTP_Check(url)
h.main()
