
from flask import Flask
# from bk_code import getWhopperCode

app = Flask(__name__)

@app.route('/')
def hello():
    # whopperCode = getWhopperCode()
    return "CB1234"

if __name__ == '__main__':
    app.run()
