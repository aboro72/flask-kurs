from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager, create_access_token, create_refresh_token,
    set_access_cookies, set_refresh_cookies,
    jwt_required, get_jwt_identity, unset_jwt_cookies
)


app = Flask(__name__)
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_SECURE'] = False
app.config['JWT_ACCESS_COOKIE_PATH'] = '/api/'
app.config['JWT_REFRESH_COOKIE_PATH'] = '/token/refresh'
app.config['JWT_COOKIE_CSRF_PROTECT'] = True
app.config['JWT_SECRET_KEY'] = '1qayXSW"3edc'

jwt = JWTManager(app)


@app.route('/token/auth', methods=['GET'])
def login():
    username = request.args.get('username', None)
    password = request.args.get('password', None)
    if username != 'admin' or password != "nimda":
        return jsonify({'login': False}), 401
    access_token = create_access_token(identity=username)
    refresh_token = create_refresh_token(identity=username)
    
    resp = jsonify({'login': True})
    set_access_cookies(resp, access_token)
    set_refresh_cookies(resp, refresh_token)
    return resp, 200


@app.route('/token/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    user = get_jwt_identity()
    access_token = create_access_token(identity=user)
    return jsonify(access_token=access_token)


@app.route('/token/remove', methods=['POST'])
def logout():
    resp = jsonify({'logout': True})
    unset_jwt_cookies(resp)
    return resp, 200


@app.route('/api/example', methods=['GET'])
def protect():
    user = get_jwt_identity()
    return jsonify({'hello World': user}), 200


if __name__ == '__main__':
    app.run(port=80, debug=True)
# Weitere Infos https://flask-jwt-extended.readthedocs.io/en/stable/refreshing_tokens/