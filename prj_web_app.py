from flask import Flask, render_template
import os
import signal
from prj_db_connector import get_user

app = Flask(__name__)


# supported methods
@app.route('/users/get_user_data/<user_id>')
def get_user_id(user_id):
    getuser = get_user(user_id)
    if getuser != "somthing went wrong":
        return f'<H1> user id: {getuser} </H1>'
    else:
        return f'<H1> no user with the specific ID {getuser} </H1>'


@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    # return "<H1> 404 </H1><p>Page not Found!</p>", 404


app.run(host='127.0.0.1', debug=True, port=5001)
