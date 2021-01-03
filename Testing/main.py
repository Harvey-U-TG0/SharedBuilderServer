from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app);
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id =  db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable = False)
    likes= db.Column(db.Integer, nullable = False)
    brickArray = db.Column(db.PickleType, nullable = True)

    def __repr__(self):
        return f"Video(name={name}, views={views}, likes={likes}, brickArray{brickArray})"

db.create_all()

# Video System Example
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name",type=str, help="Name of the video",required=True)
video_put_args.add_argument("views",type=int, help="Views of the video",required=True)
video_put_args.add_argument("likes",type=int, help="Likes of the video",required=True)
video_put_args.add_argument("brickArray",type=bytes, help="The brick array itself",required=True)


video_update_args = reqparse.RequestParser()
video_update_args.add_argument("")
video_update_args.add_argument("name",type=str, help="Name of the video")
video_update_args.add_argument("views",type=int, help="Views of the video")
video_update_args.add_argument("likes",type=int, help="Likes of the video")
video_update_args.add_argument("brickArray",type=list, help="The brick array itself",required=True)


resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer,
    'brickArray': fields.List
}


class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Could not find video with that id")
        return result

    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="Video id taken...")
        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'], brickArray=args['brickArray'])
        db.session.add(video)
        db.session.commit()
        return video, 201

    @marshal_with(resource_fields)
    def patch(self,video_id):
        args = video_update_args.parse_args()
        result = result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404,message="Video doesn't exist")
        if args['name']:
            result.name = args['name']
        if args['views']:
            result.name = args['views']
        if args['likes']:
            result.name = args['likes']
        if args['brickArray']:
            result.brickArray = args['brickArray']
 
        db.session.commit()
        return result

    def delete(self, video_id):
        
        del videos[video_id]
        return '', 204
    
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)