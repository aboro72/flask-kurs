from flask import Flask, request
from OpenSSL import SSL

context = SSL.Context(SSL.TLSv1_2_METHOD)
context.use_certificate('mycert.crt')
context.use_privatekey('myprivatekey.key')

app = Flask(__name__)

@app.route("/")
def bonus1():
    return "hello world"


if __name__ == '__main__':
    app.run(port=80, debug=True, ssl_context=context, threaded=True)
