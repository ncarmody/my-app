# "AA0WAAlCABwWAAt3AAlgABXg"
from flask import Flask
from flask_restful import Api, Resource, reqparse
# from function_col import pp
import sys
app = Flask(__name__)
api = Api(app)
port = 5000

if sys.argv.__len__() > 1:
	port = sys.argv[1]
print(port)
# pp(port)

sensorData = reqparse.RequestParser()
dictOfKeys = [["device_id", str], ["distance1", float], ["distance2", float]]
[sensorData.add_argument(i[0], type=i[1], help = str(i[0])+" is missing", required = True) for i in dictOfKeys]


# docker build -t flaskytd .

# docker run -it -p 5000:5000 flaskapp

						# {name of docker image}


class returnRequest(Resource):
	def get(self):
		return {"data":"hello world"}
	def post(self):
		args = sensorData.parse_args()
		print({"data is": args})
		return {'recieved': args}, 200


api.add_resource(returnRequest, "/request")

if __name__ == "__main__":
	app.run(host = "0.0.0.0", port=port)