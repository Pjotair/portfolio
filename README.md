# API Test Engine
***
API test engine, used to separate repetitive parts of code. Test cases can be parameterized using the `@pytest.mark.parameterrize` decorator.
The test engine validates the status code defined and the response template defined in the test (see [Checking dictionary and data types](#checking-dictionary-and-data-types) for details).
The assertion should be defined inside the test code.

The RequestsAction class provides a set of methods for making HTTP requests and handling the responses. It provides methods for GET, POST, PATCH, and DELETE requests, as well as a method for checking the data types of a dictionary.

API tests should be placed in a class that inherits the `RequestsAction` class
>from tests.helpers.qa_requests import RequestsAction

### Table of Contents
- [Technologies](#technologies)
- [Build payload](#build-payload)
- [Change dictionary](#change-dictionary)
- [Endpoint vairable](#endpoint-vairable)
- [Method GET](#method-get)
- [Method POST](#method-post)
- [Method PATCH](#method-patch)
- [Method DELETE](#method-delete)
- [Checking dictionary and data types](#checking-dictionary-and-data-types)

### Technologies
- python 3.8
- pytest 6.2.2

***
### Build payload
*build_payload()* <br> Tests that need payload in json format use the `build_payload` function, you need to pass parameters to run:
- `payload_template` (json -> dict template declared in the test variable), 
- `payload_keys` (given in test parameters -> list),
- `payload_values` (given in test parameters -> list)

The different variants of the test (positive/negative), modify the payload using the `change_dict` function.

This function accepts a dictionary `payload_template`, a list of strings `payload_keys`, and a list of Any type `payload_values`. It creates a new list by zipping `payload_keys` and `payload_values` and calls the `change_dict` function for each key-value pair in the new list. It returns the modified `payload_template`.

***
### Change dictionary
*change_dict()* <br> The function changes the value for the selected key in the dictionary. It supports a dictionary with different levels of nesting.

This function accepts a dictionary `payload_template`, a string `search_key`, and an Any type `new_value`. It iterates through the dictionary and replaces the value of the key that matches `search_key` with `new_value`. It also checks for nested dictionaries and recursively calls itself for those nested dictionaries. It returns the modified `payload_template`.

***
### Endpoint vairable
The endpoint is built for a specific test and then passed to the request function.
For example:
>endpoint = f'customers{uuid}/location/{uuid}'

Possible query params are passed to the request function as a separate argument `**param_dict`.

***
### Method GET
*qa_get()* <br> This function makes a GET request to the specified `api_url` and `endpoint` using the `api_client` object. It returns a tuple containing the status code and the JSON response body.

***
### Method POST
*qa_post()* <br> This function makes a POST request to the specified `api_url` and `endpoint` using the `api_client` object, including the specified `body_payload` and `param_dict` as the request body and query parameters respectively. It returns a tuple containing the status code and the JSON response body.

***
### Method PATCH
*qa_patch()* <br> This function makes a PATCH request to the specified `api_url` and `endpoint` using the `api_client` object, including the specified `body_payload` and `param_dict` as the request body and query parameters respectively. It returns a tuple containing the status code and the JSON response body.

***
### Method DELETE
*qa_delete()* <br> This function makes a DELETE request to the specified `api_url` and `endpoint` using the `api_client` object. If the status code of the response is not 204, it returns a tuple containing the status code and the JSON response body. Otherwise, it returns a tuple containing the status code and None.

***
### Checking dictionary and data types
*check_dict_data_types()* <br> This function checks if the data types of the `response_body` match the data types specified in the `response_template`.

The data type in the value must be inside the list. It is possible that the answer will store a type such as int or float (this may be acceptable). Specify in the response_template dictionary the data types that can be valid.

Example `response_template`: 

    response_template = {
            "drop": {"percentage": [int, float], "value": [int]},
            "pmCycles": {"percentage": [int, float], "value": [int]},
            "lipDown": {"percentage": [int, float], "value": [int]},
            "slowOperation": {"percentage": [int, float], "value": [int]}
        }

Arguments
* response_template: A dictionary representing the template of the expected response.
* response_body: A dictionary representing the actual response received.

Returns:
* Returns True if the data types in the response_body match the data types in the response_template.
* Returns False if the data types in the response_body do not match the data types in the response_template.

How it works:

The function iterates through each key-value pair in the response_template dictionary. For each key, it checks if the key exists in the response_body dictionary. If not, it returns False. If the value of the key in the response_template is a dictionary, it calls itself recursively with the nested dictionaries. If the value is not a dictionary, it checks if the type of the value in the response_body is a subclass of any of the data types specified in the value of the corresponding key in the response_template. If it does not match any data type in the response_template, it returns False. If all checks pass, it returns True.

--
--
