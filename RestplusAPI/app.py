from flask import Flask, Blueprint
from RestplusAPI import settings
from RestplusAPI.api.myapi import api
from RestplusAPI.api.shop.endpoints.products import namespace as productsnamespace

app = Flask(__name__)


def configure_app(app):
    app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_EXPANSION
    app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VAL
    app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER


def init_app(app):
    configure_app(app)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(productsnamespace)
    app.register_blueprint(blueprint)


def main():
    init_app(app)
    app.run(debug=settings.FLASK_DEBUG, threaded=settings.FLASK_THREADED)


if __name__ == '__main__':
    main()