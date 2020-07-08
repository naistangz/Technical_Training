# JSON API with Python :closed_lock_with_key:

## What is JSON? Javascript Object Notation 
- Minimal, readable format for structuring data.
- Used to transmit data between server and web application, as an alternative to XML (e**X**tensible Markup Language).
- It is a way to store information in an organised, easy-to-access manner.
- It gives us human-readable collection of data that we can access in a logical manner. 


## The Python JSON Module
- The JSON module is part of the built in Python library and contains methods for working with the format.
- There are two methods for parsing text into JSON. `LOAD` and `LOADS`.
- There are two methods for taking python objects and serialising them directly into `JSON`, `dump` and `dumps`.

## Why does JSON matter?
- JSON feeds from other sites via AJAX (Asynchronous JavaScript and XML). Many sites are sharing data using JSON in addition to RSS (Really Simple Syndication) feeds.
- JSON feeds can be loaded **asynchronously** much more easily than XML/RSS.

## Keys and Values 
The two primary parts that make up JSON are keys and values. 
Together they make a key/value pair. 

- **Key:** A key is always a string enclosed in quotation marks.
- **Value:** A value can be string, number, boolean expression, array, or object.
- **Key/Value Pair:** A key value pair follows a specific syntax, with the key followed by a colon followed by the value. Key/Value pairs are comma separated.

```json
"foo":"bar"
```
This is a key/value pair. The key is "foo" and the value is "bar".

## Types of Values
- **Array:** Associative array of values
- **Boolean:** True or False
- **Number:** Integer
- **Object:** Associative array of key/value pairs
- **String:** Several plain text characters which usually form a word.

**Objects**
- An object is indicated by curly brackets. Everything inside of the curly brackets is part of the object. 

```json
"hello" : {
  "foo": "bar"
}
```
The key/value pair "foo":"bar" is nested inside the key/value pair "hello":{ ... }. This is an example of a hierarchy in JSON data.

## Serialising JSON
When a computer processes lots of information, it needs to take a data dump. The `json`library exposes the `dump()` method for writing data to files.
Simple python objects are translated to JSON accordingly. 
Python - JSON -> `DUMP`

**Python**|**JSON**
--------|-------
dict|object
list, tuple|array
str|string
int, long, float|number
True| true
False|false
None|null

```python
import json
car_data = {"name": "tesla", "engine": "electric"}
car_data_json_string = json.dumps(car_data)
with open("new_json_file.json", "w") as jsonfile:
    # opening a new file called new_json_file.json, permission type write 'w'
    # jsonfile as the alias
    # Encoding and writing into json file

    json.dump(car_data, jsonfile)
    #json.dump takes 2 args
    # first argument is dictionary, second argument is file_type (jsonfile)
```

## Deserialising JSON
In the `json` library, `load()` and `loads()` turn JSON encoded data into Python objects.

`JSON` to Python object -> `LOAD`

**JSON**|**Python**
--------|-------
object|dict
array|list, tuple
string|str
number(int)|int
number(real)|float
true|True
false|False
null|None|

```python
with open("new_json_file.json") as jsonfile:
    # Decoding
    # Reading the file we have created
    car = json.load(jsonfile)

    print(type(car))
    # checking the type of data again

    print(car['name']) # to get the value stored in the key called 'name'
    print(car['engine']) # to get the value of second key value pair
```

## HTTP Request Structure

![HTTP_Request Structure](../images/http_request.png)


## HTTP Response
HTTP response status codes indicate whether a specific HTTP request has been successfully completed. Responses are grouped in five classes:

1. Informational responses (`100`-`199`)
2. Successful responses (`200`-`299`)
3. Redirects (`300`-`399`)
4. Client errors (`400`-`499`)
5. Server errors (`500`-`509`)

* 100 Continue. The client SHOULD continue with its request
* 200 OK. The request has succeeded
* 203 Non-Authoritative Information
* 206 Partial Content
* 300 Multiple Choices
* 303 See Other
* 306 (Unused) 
* 400 Bad Request

[Click Here for infographic](../images/http-decision-diagram.png)

## Comparing JSON to XML style:

**JSON style:**

```bash
{"students":[
    {"name":"John", "city:" Agra},
    {"name":"Steve", "city":"Santiago"},
    {"name":"Peter", "city":"Madrid"},
    {"name": "Anais", "city":"Paris"}
]}
```

**XML Style:**

```xml
<students>
  <student>
    <name>John</name><city>Agra</city>
  </student>
  <student>
    <name>Steve</name><city>Santiago</city>
  </student>
  <student>
    <name>Peter</name><city>Madrid</city>
  </student>
  <student>
    <name>Anais</name> <city>Paris</city>
  </student>
</students>
```

JSON is light-weighted compared to XML. In JSON we can also take advantage of arrays that is not available in XML>

## Exercises with JSON

- [x] [JSON Exchange Rates](json_exchange_rates.py)
- [x] [JSON Encoding and Decoding](json_encoding_decoding.py)
- [x] [JSON parsing with API](json_parsing_with_api.py)
- [x] [JSON_Parse_start](json_parse_start.py)
- [x] [JSON Serialize Start](json_serialize_start.py)

## JSON exception handling 
- [x] [JSON error handling](../Error_Handling/json_err_finished.py)