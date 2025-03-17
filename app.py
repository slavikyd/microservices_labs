"""MS hw flask server."""
from flask import request
import randomer
import http_code
from creds import app
from extras import WELCOME_PAGE, body_check



@app.get('/')
def welcomingpage():
    """Welcome page handler.

    Returns:
        str: html string of welcome page
    """
    return WELCOME_PAGE


@app.get('/api/v1/contact')
def get_contact():
    """Get request handler for contacts.

    Returns:
        cursor: in fetchall state
        int: http-code answer
    """
    try:
        return f"{randomer.random_contact()}", http_code.OK
    except Exception as e:
        print(e)
        return '', http_code.SERVER_ERROR


@app.post('/api/v1/contact')
def create_contact():
    """Post request handler for contacts.

    Returns:
        str: empty string
        int: http-code answer
    """
    #body = request.json()
    try:
        return randomer.random_contact().__str__(), http_code.OK
    except Exception:
        return http_code.SERVER_ERROR


@app.route('/api/v1/contacts', methods=['GET', 'POST', 'PUT'])
def update_contact():
    """Handler for GET, POST, and PUT requests to update contacts.

    Returns:
        str: random contact
        int: http-code answer
    """
    try:
        if request.method == 'PUT':
            # Example of accessing the request body
            body = request.json
            print("Received body:", body)
        return randomer.random_contact(), http_code.OK
    except Exception as e:
        print(e)
        return '', http_code.SERVER_ERROR


@app.delete('/api/v1/contact')
def delete_contact():
    """Post request handler used to delete contacts and links.

    Returns:
        str: empty str
        int: http-code answer
    """
    #body = request.json



    return 'Deleted', http_code.NO_CONTENT


@app.get('/api/v1/group')
def get_group():
    """Get request handler for groups.

    Returns:
        cursor: in fetchall state
        int: http-code answer
    """
    try:
        return randomer.random_group().__str__(), http_code.OK
    except Exception:
        return http_code.SERVER_ERROR


@app.post('/api/v1/group')
def create_group():
    """Post request handler for groups.

    Returns:
        str: empty string
        int: http-code answer
    """
    body = request.json()
    try:
        return randomer.random_group().__str__(), http_code.OK
    except Exception:
        return http_code.SERVER_ERROR


@app.put('/api/v1/groups')
def update_group():
    """Put request handler used to update groups.

    Returns:
        str: empty string
        int: http-code answre
    """
    body = request.json()


    try:
        return randomer.random_group().__str__(), http_code.OK
    except Exception:
        return http_code.SERVER_ERROR


@app.delete('/api/v1/group')
def delete_group():
    """Post request handler used to delete group and links.

    Returns:
        str: empty str
        int: http-code answer
    """
    body = request.json


    return 'Deleted', http_code.NO_CONTENT



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6080)