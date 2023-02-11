from flask import Flask, request

from prj_db_connector import add_user, get_user, put_user, delete_user

app = Flask(__name__)


# supported methods
@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'POST':
        # getting the json data payload from request
        request_data = request.json

        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        adduser = add_user(user_id, user_name)
        if adduser != "somthing went wrong":
            return {'user id': user_id, 'user name': user_name, 'status': 'ok'}, 200

        else:
            return adduser

    elif request.method == 'PUT':
        # getting the json data payload from request
        request_data = request.json

        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        putuser = put_user(user_id, user_name)
        if putuser != "somthing went wrong":
            return {'user id': user_id, 'user name': user_name, 'status': 'ok'}, 200
        else:
            return putuser

    elif request.method == 'DELETE':

        # treating request_data as a dictionary to get a specific value from key
        deluser = delete_user(user_id)
        if deluser != "somthing went wrong":
            return {'user id': user_id, 'status': 'ok'}, 200
        else:
            return deluser

    elif request.method == 'GET':
        # treating request_data as a dictionary to get a specific value from key
        getuser = get_user(user_id)
        if getuser != "somthing went wrong":
            return {'user name': getuser, 'status': 'ok'}, 200
        else:
            return getuser



# todo elif for get put and delete


app.run(host='127.0.0.1', debug=True, port=5000)
