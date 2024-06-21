from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
# from sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/flask-restful'
db = SQLAlchemy(app)

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

# Get the data from url
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the Video", required=True)
video_put_args.add_argument("views", type=int, help="Views of the Video", required=True)
video_put_args.add_argument("likes", type=int, help="Likes of the Video", required=True)

videos = {}

def VideoNotExist(video_id) :
    if video_id not in videos:
        abort(404, message="Video id is not exist...")

def VideoisExist(video_id) :
    if video_id in videos:
        abort(409, message="Video already exist... ")

class Video(Resource):
    def get(self, video_id) :
        VideoNotExist(video_id)
        return videos[video_id]
    
    def put(self, video_id) :
        VideoisExist(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201
    
    def delete(self, video_id) :
        VideoNotExist(video_id)
        del videos[video_id]
        return '', 204


api.add_resource(Video, "/video/<int:video_id>")

# Connecting into local database
class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    like = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name = {name}, views = {views}, likes = {likes})"

# Create all database tables
with app.app_context():
    db.create_all()
    

# Running the flask app
if __name__ == "__main__":
    app.run(debug=True)