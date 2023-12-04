def create_error_response(details):
    response = {"status": "error", "details":details}
    return response

def create_ok_response(details):
    response = {"status": "ok", "details":details}
    return response