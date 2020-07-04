# REST APIs

## Status Codes

Status codes are returned with a response after each call to the server. They briefly describe the result of the call. 

- **200 - OK** The request was successful. The answer itself depends on the method used (GET, POST, etc) and the API specification.

- **204 - No Content** The server successfully processed the request and did not return any content. 

- **301 - Moved Permanently** The server responds that the requested page (endpoint) has been moved to another address and redirects to this address.

- **400 - Bad Request** The server cannot process the request because the client-side errors (incorrect request format)

- **401 - Unauthorised** Occurs when authentication was failed, due to incorrect credentials or even their absence. 

- **403 - Forbidden** Access to the specified resource is denied. 

- **404 - Not Found** The requested resource was not found on the server.

- **500 - Internal Server Error** Occurs when an unknown error has occurred on the server.

The **request** library has useful properties for working with status codes. For example, you can simply view the status of the response code by accessing.status_code:

```python 
print(response.status_code)
>>> 200
```

**Control flow statement**
Will evaluate to `True` if the status code was between 200 and 400, and `False` otherwise.

```python 
if response:
    print("Response is successful.")
else:
    print("Response returned an error.")
```

## Endpoints

**What is an API endpoint?**
- The point of entry in a communication channel when two systems are interacting. It refers to touchpoints of the communication between an API and a server.
- Endpoint is the means from which the API can access the resources they need from a server to perform their task. 
- The URL of a server or service. 

- APIs operate through 'requests' and 'responses'
- When API requests to access data from a web application or server, a response is always sent back. 
- The location of where the API sends a request and where the response emanates is the **endpoint**
- Endpoint is the most crucial part of the API documentation - it is what the developer will implement to make their requests.

## API vs Endpoint

[Incomplete notes](https://rapidapi.com/blog/api-glossary/endpoint/)