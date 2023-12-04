from flask import Flask, json, request
import apis
import logger

server_app = Flask(__name__)

SERVER_PORT = 8080

@server_app.route('/api', methods=['POST'])
def run_api():
    try:
        # Extract API name and arguments
        if "api_name" in request.json:
            api_name = request.json["api_name"]
            args = request.json["args"] if "args" in request.json else {}        
            # Execute the API
            api_result = apis.APIs.execute(api_name, args, b_execute=False)
        else:
            api_result = {"is_valid": False, "validation_errors":"Malformed request. POST JSON does not contain API name. API name should be specified as 'api_name'."}
        
        # Return execution result
        http_response_status = 400 
        if api_result["is_valid"]:
            http_response_status = 200 
        
        http_response = server_app.response_class(
            response = json.dumps(api_result),
            status = http_response_status,
            mimetype = 'application/json'
        )
        return http_response
    except Exception as e:
        http_response = server_app.response_class(
            response = {"is_valid": False, "validation_errors":"Internal Server Error: " + str(e)},
            status = http_response_status,
            mimetype = 'application/json'
        )
        return http_response




if __name__ == '__main__':
      server_app.run(host='0.0.0.0', port=SERVER_PORT)