from flask_restplus import Api

api = Api(version='0.1', title='My Demo API', description='Please modify this API')


@api.errorhandler
def std_handler(e):
    return {'message': 'An unexpected error has occurred. Please call the support.'}, 500

