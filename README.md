# To-Do. Write the docs after the Architecture is decided.

## PCHEM Service

This project provides an HTTP service to remotely interact with the Propsim emulator. The service executes AT commands at the Propsim over a TCP connection, and returns the response after execution.

Each AT command is exposed as a distinct API, e.g. the "get_version" API executes the corresponding AT command to query the version ("syst:vers?\n") over TCP at Propsim, and returns the result to the user. Users interact with the HTTP service using POST requests and specify the API name and API arguments, if any, within the POST request body in JSON format. The response of the AT command execution is provided in JSON format in the body of the HTTP POST response. You can find the required format of the POST request and the provided format of POST response in the user documention.

## Docs for users and developers
The document for users of the PCHEM service is located at <>
The document for developers of the PCHEM service is located at <>