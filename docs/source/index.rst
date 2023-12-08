.. PCHEM documentation master file, created by
   sphinx-quickstart on Thu Dec  7 19:49:00 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to PCHEM's documentation!
=================================
This project provides an HTTP-based service to allow users to remotely interact with the Propsim Radio Frequency (RF) emulator. 

The service exposes various APIs, which can be called using an HTTP POST request. Each API executes a specific AT command at the Propsim emulator over a TCP connection, and returns the response to the user after execution. E.g. the "get_version" API executes the corresponding AT command ("syst:vers?\\n" in this case), over TCP at Propsim, to query the version and returns the same within the HTTP response to the user.

Users specify the API name and API arguments, if any, within the POST request body in JSON format. The response of the AT command execution is provided back to the user in JSON format in the body of the HTTP POST response. You can find the required format of the POST request and the provided format of POST response in the user documention.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   users
   developers
   installation
   apis


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
