from flask_restful import Resource, reqparse

class ControllerBase(Resource):
    parser = reqparse.RequestParser(bundle_errors=True)
    parser.add_argument('authorization', required=False, type=str, location ='headers')
    
# ags - url https://myservice.com/api/v1/state?id=2
#json - в теле запроса

