from flask import Flask,jsonify,request
from stars_data import data

app = Flask(__name__)
@app.route("/")
def index():
    return jsonify({
        "stars_data":data,
        "message":"success"
    }),200

@app.route("/star")
def star():
    name = request.args.get("name")
    star_data = next(i for i in data if i["name"] == name)
    return jsonify({
        "stars":star_data,
        "message":"success"
    }),200

app.run()
