from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Basic get method
class HelloWorld(Resource):
    def get(self) :
        return {
            "data" : "Hello World",
            "status" : "good",
            "message" : "yes"
                }
    def post(self) :
        return {
            "data" : "Hellow World",
            "status" : "Success",
            "message" : "Successful"
        }
    
api.add_resource(HelloWorld, "/helloworld")

# Getting the data from Parameter
class Params(Resource):
    def get(self, username, status) :
        return {
            "data" : "good",
            "username" : username,
            "status" : status            
        }

api.add_resource(Params, "/params/<string:username>/<int:status>")

# Getting the data from the variable
names = {
    "fahmi" : {
        "age" : 19,
        "status" : True,
        "IQ" : 199
        },
    "not-fahmi" : {
        "age" : 23,
        "status" : False,
        "IQ" : 100
    }
}

class PassingFromVar(Resource):
    def get(self, name) :
        return names[name]

api.add_resource(PassingFromVar, "/var/<string:name>")

# Running the flask app
if __name__ == "__main__":
    app.run(debug=True)