
from flask import Flask, render_template, jsonify
from bk_code import getWhopperCode
from dotenv import load_dotenv
from os import environ
load_dotenv()

app = Flask(__name__)

@app.route('/')
def root():
    return render_template("index.html")

@app.route('/api/code', methods=['GET'])
def code():
    whopperCode = getWhopperCode()
    return jsonify({"code":whopperCode})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000 if environ.get("MODE") == "dev" else 80)
