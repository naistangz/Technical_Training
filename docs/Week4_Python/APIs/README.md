# APIs

### What is an API?
**A**pplication **P**rogramming **I**nterface 
- An API is a set of programming instructions and standards for accessing a web-based software application or **web tool**
- An API is a software-to-software interface, not a user interface.
- Applications talk to each other without any user knowledge or intervention. 
- APIs defines the rules that programmers *must* follow in order to interact with a programming language, a software library, or any other software tool.
- Allows two unrelated systems to interact with each other.

### API set of specifications?
- API typically defined as set of specifications, such as HTTP request messages, along with definition of the structure of response messages, usually in Extensible Markup Language (XML) or JavaScript Object Notation (JSON) format.
- API specification describes the way that each of the two systems must interact with the API itself (such as language that must be used, the syntax, etc)
- Example: shipping company API that can be added to an eCommerce-focused website to facilitate ordering shipping services and automatically include current shipping rates, without site developer having to enter the shipper's rate table into a web database.

### Example of an API?
- When using an application on a mobile phone, the application connects to the Internet and sends data to a server.
- The server retrieves that data, interprets it, performs the necessary actions and sends it back to your phone. 
- The application interprets that data and presents you with the information you want in a readable way. 

### What is web scraping?
- Data scraping used for extracting data from websites 
- Refers to automated processes implemented using a bot or web crawler
- Some websites can contain very large amount of invaluable data such as stock prices, product details
    - Web scraping allows developers to extract and export data in a format that is more useful for the user. In the form of a spreadsheet or an API.

**Analogy**
[Extracted from Mulesoft](https://www.mulesoft.com/resources/api/what-is-an-api)
- Using a restaurant as an analogy, the kitchen is the part of the "system" that will prepare your order. What is missing the critical link to communicate the order to the kitchen and deliver the **food** back to your table. That is where the waiter or API comes in. The waiter is the messenger - or API - takes the request or order and tells the kitchen, the system what to do. The waiter delivers the response back (the food).

### APIs everywhere
**Travel APIs**
- When booking a flight on an airline website, you can choose a departure city and date, a return city and date, cabin class as well as other variables. 
- To book flights, you interact with the airline's website to access their database and see if any seats are available on those dates and what the costs might be.

**Skyscanner, Expedia, Kayak**
- If you are not using the airline's website, the travel services interacts with the airline's API..
- The API is the interface that online travel services like skyscanner use to get information from the airline's database to book seats, baggage options, flight options, etc. 
- Skyscanner's Travel API then takes the airline's response to your request, which shows the most updated, relevant information. 

<img src="https://i.stack.imgur.com/WSYOk.png" alt="skyscanner_api">

### Why use an API?
- APIs allow developers to access a library of an app's existing information by using a key. 
- APIs are re-usable, secure and more manageable.
- No need to open up database to direct client connections and manage those connections. 
- Extends functionality of a web server.
- Useful when dealing with data that changes constantly like stock prices and weather. 

### Why are APIs important?
**1. APIs are huge time-savers**

**2. Businesses are creating apps that rely on APIs**

**3. APIs help businesses**
- Web APIs allow businesses to access 3rd part data and seamlessly integrate it anywhere and anytime it is required. 
- E.g. Facebook APIs provide businesses with a single sign-on mechanism across web, mobile and desktop apps.

### When is it important to create an API?

In general, it is best to consider an API if:
1. Your data set is large, making download via FTP (File Transfer Protocol) resource-intensive. 
2. Users need access to data in real time, such as for display on another website or as part of an application. 
3. Your data changes or is updated frequently e.g. weather, corona virus cases
4. Your users only need access to a part of the data at any one time. 
5. Your users will need to perform actions other than retrieve data, such as contributing, updating, or deleting data.




**Installing python package in Pycharm**

`pip install requests`

### The Modern API (HTTP and REST)

- Modern APIs adhere to standards (typically HTTP and REST).
- They are treated more like products than code. They are designed for consumption for specific audiences (e.g. mobile developers), they are documented, and they are version in a way that users can have certain expectations of its maintenance and lifecycle. 
- Because they are *standardised*, they have a much stronger discipline for security and governance, as well as monitored and managed for performance and scale.

**Defining APis**
- An API is a set of rules that are shared by a particular service.
- These rules determine in which format and with which command set your application can access the service, as well as what data this service can return in the response.
- The API acts as a layer between your application and external service.
- You do not need to know the internal structure and features of the service, you just send a certain simple command and receive data in a predetermined format.

**REST API** is an API that uses HTTP requests for communication with web services. 

It complies with the following constraints:
1. **Client-server architecture** - the client is responsible for the user interface, and the server is responsible for the backend and data storage. Client and server are independent and each of them can be replaced.

2. **Stateless** - No data from the client is stored on the server side. The session state is stored on the client side. 

3. **Cacheable** - Clients can cache server responses to improve performance. 


### Using APIs with Python
REST API can be viewed as a data source located on an internet address that can be accessed in a certain way through certain libraries.

**Types of Requests**
Types of Requests or HTTP request methods characterise what action we are going to take by referring to the API.

- **GET:** retrieve information. The most common type of request. 

```python
response_bbc = requests.get("https://www.bbc.co.uk/")
print(response_bbc)
# Returns <Response [200]>
```
- **POST:** adds new data to the server, such adding a new item to your inventory. 

- **PUT:** changes existing information such as changing the colour or value of an existing product. 

- **DELETE:** deletes existing information

> Prerequisites and Status Codes [HERE](restAPI_python.md)

### HTTP and HTTPs
**Checking HTTP/HTTPS status**
* 200  Success
* 400 
* 404 Page not found 


[Click Here for Infographic](../images/http-decision-diagram.png)

### Using Requests
* Simple API - each HTTP verb is a method name 
* Makes working with parameters, headers, and cookies easier
* Automatically decodes returned content
* Automatically parses JSON content when detected
* Handles redirects, timeouts, and errors
* Supports advanced features like authentication and sessions

**Importing the requests module in pycharm**

```python
import requests
```

### Making a simple requests
```python
response = requests.get(url)
```

**params**|Key-value pairs that will be sent in the query string
-------|--------
**headers**| Dictionary of header values to send along with the request
**auth**| Authentication tuple to enable different forms of authentication
**timeout**| Value in seconds to wait for the server to respond 

Exercise file [HERE](python_requests_module.py)

---
Practical resources: [Codecademy Learn the Watson API](https://www.codecademy.com/learn/ibm-watson)

