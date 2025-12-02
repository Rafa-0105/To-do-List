from flask import Flask, jsonify

from DB.conection import conn

app = Flask(__name__)

@app.route("/teste", methods=['GET'])
def api_get():
    get_db = conn()
    return jsonify("Conection on DataBase sucess!"), 200
