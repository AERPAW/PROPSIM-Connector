import requests

LIBRARY_IP = "127.0.0.1"
LIBRARY_PORT = 8080

def dummy_api(arg1):
    # Make an HTTP request to the Propsim library
    api_name = "dummy_api"
    api_args = locals()
    http_response = requests.post("http://" + LIBRARY_IP + ":" + str(LIBRARY_PORT) + "/api", 
                            json={"api_name": api_name, "args":api_args})
    print(http_response)
    library_response = http_response.json()
    return library_response

dummy_api("arg1-value")