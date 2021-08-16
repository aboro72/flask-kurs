from flask import Flask, request, jsonify

import werkzeug
import json

app = Flask(__name__)


@app.route("/")
def bonus1():
    return "hello world"


@app.route("/logging/")
def bonus2():
    app.logger.info("Information")
    return "hello world"


@app.route("/postme/", methods=['POST'])
def bonus3():
    postedjson = json.loads(request.data.decode("utf-8"))
    postedjson["data"]
    print(postedjson)
    return "passt schon"


@app.errorhandler(werkzeug.exceptions.NotFound)
def notfound(e):
    return jsonify(error=str(e)), e.code
# oder
#   return 'diedeldum du bist dumm', e.code
#   oder what ever


if __name__ == '__main__':
    app.run(port=80, debug=True, threaded=True)