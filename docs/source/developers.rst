Developers Document
###########################

| This section is meant for developers of the PCHEM Service, who want to write a new API. 

| Below are the steps to write a new PCHEM API:

#. Define an api client within ``client.py``, which will make an HTTP call to the PCHEM service: Refer to existing APIs within ``client.py``. Define a function with the desired API name and input arguments. Form a json object from the input arguments and pass it as an argument, along with the API name to ``call_api()``. Receive the PCHEM response from ``call_api()`` and return it from your function. The framework includes the Propsim AT command response within the response from ``call_api()``. 

#. Define an api validator within ``validators.py``: Refer to existing API validators within ``validators.py``. Define a function with the desired API name. The function must receive ``args`` as input. ``args`` is a python dictionary containing the input arguments, as defined by you in Step 1. Validate ``args`` as required, e.g. check if the argument values are within the range required for Propsim. Return an object with two keys: 1. ``is_valid``, whose value is True or False depending on the validation result. 2. ``validation_errors`` whose value is of type string, describing the errors, if any. If no validation is required, return ``no_validation()``.

#. Define the api within ``apis.py``: Refer to existing API definitions within ``apis.py``. Define a function with desired API name. The function must receive ``args`` as input. Create the AT command, of data type string, from the input arguments, if any. Return this AT command string from your function.

#. Test and verify that your API works as intended.

#. Update the API documentation, located at ``docs/source/apis.rst`` to describe your API.
