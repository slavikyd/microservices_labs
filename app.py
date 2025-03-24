from flask import request
import randomer
import http_code
from creds import app
from extras import WELCOME_PAGE
import json

@app.route('/', methods=['GET'])
def welcomingpage():
    return WELCOME_PAGE

@app.route('/api/v1/contacts', methods=['GET'])
def get_contacts():
    response = randomer.random_contact()
    try:
        return json.dumps(response.__dict__, default=str), http_code.OK
    except Exception as e:
        print(e)
        return '', http_code.SERVER_ERROR

@app.route('/api/v1/contacts', methods=['POST'])
def create_contacts():
    response = randomer.random_contact()
    try:
        return json.dumps(response.__dict__, default=str), http_code.OK
    except Exception:
        return '', http_code.SERVER_ERROR

@app.route('/api/v1/contacts', methods=['PUT'])
def update_contacts():
    response = randomer.random_contact()
    try:
        return json.dumps(response.__dict__, default=str), http_code.OK
    except Exception as e:
        print(e)
        return '', http_code.SERVER_ERROR

@app.route('/api/v1/contacts', methods=['DELETE'])
def delete_contacts():
    return 'Deleted', http_code.NO_CONTENT

@app.route('/api/v1/group', methods=['GET'])
def get_group():
    response = randomer.random_group()
    try:
        return json.dumps(response.__dict__, default=str), http_code.OK
    except Exception:
        return '', http_code.SERVER_ERROR

@app.route('/api/v1/group', methods=['POST'])
def create_group():
    response = randomer.random_group()
    try:
        return json.dumps(response.__dict__, default=str), http_code.OK
    except Exception:
        return '', http_code.SERVER_ERROR

@app.route('/api/v1/group', methods=['PUT'])
def update_group():
    response = randomer.random_group()
    try:
        return json.dumps(response.__dict__, default=str), http_code.OK
    except Exception:
        return '', http_code.SERVER_ERROR

@app.route('/api/v1/group', methods=['DELETE'])
def delete_group():
    return 'Deleted', http_code.NO_CONTENT

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6080)
