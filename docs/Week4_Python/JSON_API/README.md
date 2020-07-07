# JSON API with Python :closed_lock_with_key:

## What is JSON? Javascript Object Notation 
- Minimal, readable format for structuring data.
- Used to transmit data between server and web application, as an alternative to XML (e**X**tensible Markup Language).
- It is a way to store information in an organised, easy-to-access manner.
- It gives us human-readable collection of data that we can access in a logical manner. 

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

[Click Here for infographic](../images/http-decision-diagram.png)

## Exercises with JSON

-[x] [JSON Exchange Rates](json_exchange_rates.py)

-[x] [JSON Encoding and Decoding](json_encoding_decoding.py)

-[x] [JSON parsing with API](json_parsing_with_api.py)