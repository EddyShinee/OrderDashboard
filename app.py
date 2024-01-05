from flask import Flask, render_template, jsonify
import time
from UserAccount.UserAccount import UserAccount
from Host.Hosts import Hosts

app = Flask(__name__)


# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/get_data', methods=['GET'])
def get_data():
    timestamp_ms = int(time.time() * 1000)
    data = {"message": timestamp_ms}
    return jsonify(data)


@app.route('/get_token', methods=['GET'])
def get_token():
    user_account = UserAccount()
    token = user_account.get_token()
    data = {"message": token}
    return jsonify(data)


@app.route('/get_account_summary', methods=['GET'])
def get_account_summary():
    user_account = UserAccount()
    user_account_summary = user_account.get_account_summary()
    string = user_account_summary['balance']
    data = {"message": string}
    return jsonify(data)


@app.route('/ping_host', methods=['GET'])
def ping_host():
    host = Hosts()
    host = host.ping_host()
    # data = {"message": host}
    return jsonify(host)


@app.route('/get_account_opened_order', methods=['GET'])
def get_account_opened_order():
    user_account = UserAccount()
    user_account_opened_order = user_account.get_account_opened_order()
    data = {"message": user_account_opened_order}
    return jsonify(data)


if __name__ == '__main__':
    app.run()
