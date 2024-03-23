Developers Document
###########################

| This section is meant for developers of the PCHEM Service, who want to write a new API. 

| Below are the steps to write a new PCHEM API:

#. Modify ``client.py`` as follows: Refer to existing APIs within ``client.py``. Define a function with the desired API name and input arguments. Form a json object from the input arguments and call ``call_api()``. Receive the response from ``call_api()`` and return it from your function.


#. Modify ``validators.py`` as follow: Refer to existing API validators within ``validators.py``. Define a function with the desired API name. The function must receive ``args`` as input. Validate ``args`` as required, e.g. check if the argument values are within the range required for Propsim. Return an object with two keys: 1. ``is_valid``, whose value is True or False depending on the validation result. 2. ``validation_errors`` whose value is of type string, describing the errors, if any. If no validation is required, return ``no_validation()``.


#. Modify ``apis.py`` as follows: Refer to existing API definitions within ``apis.py``. Define a function with desired API name. The function must receive ``args`` as input. Create the AT command, of data type string, from the input arguments, if any. Return this AT command string from your function.


#. Verify that your API works as intended.


#. Update the API documentation, located at ``docs/source/apis.rst`` to describe your API.
