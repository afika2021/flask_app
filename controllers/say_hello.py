from flask_restful import Resource


class SayHello(Resource):
    def get(self):
        return {
            'error': 0,
            'message': 'OK',
            'data': {
                'answer': 'Hello'
            }
        }, 200