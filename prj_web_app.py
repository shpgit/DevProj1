from flask import Flask, request, render_template
from prj_db_connector import get_user

app = Flask(__name__)


# supported methods
@app.route('/users/get_user_data/<user_id>')
def get_user_name(user_id):

    get_user(user_id)

    return "<H1> 'user_id' </H1>"


app.run(host='127.0.0.1', debug=True, port=5000)