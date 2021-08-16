from flask import Flask, request, jsonify
from OpenSSL import SSL
import werkzeug

app = Flask(__name__)


@app.route("/")
def bonus1():
    return "hello world"


@app.route("/logging/")
def bonus2():
    app.logger.info("Information")
    return "hello world"


@app.errorhandler(werkzeug.exceptions.NotFound)
def notfound(e):
    return jsonify(error=str(e)), e.code
# oder
#   return 'diedeldum du bist dumm', e.code
#   oder what ever


if __name__ == '__main__':
    app.run(port=80, debug=True, threaded=True)