from flask_restful import Resource


class ServerVersion(Resource):
    def get(self):
        return {
            'error': 0,
            'message': 'OK',
            'data': {
                'server version': '1.0.0'
            }
        }, 200
    