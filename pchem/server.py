from flask import Flask, json, request
import apis
import constants
import toml
import logger

CONFIG_PATH = "./config.toml"

server_app = Flask(__name__)

@server_app.route('/api', methods=['POST'])
def run_api():
    try:
        print(request.json)
        # Extract API name and arguments
        if constants.API_NAME_KEY in request.json:
            api_name = request.json[constants.API_NAME_KEY]
            args = request.json[constants.API_ARGS_KEY] if constants.API_ARGS_KEY in request.json else {}        
            # Execute the API
            b_api_exists = hasattr(apis, api_name) and callable(getattr(apis, api_name))
            if b_api_exists:
                api_func = getattr(apis, api_name)
                api_result = api_func(args)
            else:
                api_result = {constants.IS_VALID_KEY: False, constants.VALIDATION_ERRORS_KEY:"API not implemented."}
        else:
            api_result = {constants.IS_VALID_KEY: False, constants.VALIDATION_ERRORS_KEY:"Malformed request. POST JSON does not contain API name. API name should be specified as 'api_name'."}
        
        # Return execution result
        http_response_status = 400 
        if api_result[constants.IS_VALID_KEY]:
            http_response_status = 200 
        
        http_response = server_app.response_class(
            response = json.dumps(api_result),
            status = http_response_status,
            mimetype = 'application/json'
        )
        return http_response
    except Exception as e:
        http_response = server_app.response_class(
            response = {constants.IS_VALID_KEY: False, constants.VALIDATION_ERRORS_KEY:"Internal Server Error: " + str(e)},
            status = http_response_status,
            mimetype = 'application/json'
        )
        return http_response

if __name__ == '__main__':
      with open(CONFIG_PATH, 'r') as f:
            config = toml.load(f)
            pchem_port = config["pchem_server"]["port"]
            server_app.run(host='0.0.0.0', port=pchem_port)