from flask import Flask
from flask_restful import Resource, Api
from routes import InitRoutes

app = Flask(__name__)
api = Api(app)

InitRoutes(api)

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)

