# BUILD A REST API USING PYTHON AND FLASK-RESTful

#incorporates separation of concerns and industry best practices
#simplifies code maintainability

#also see:	
	#exception handling
	#authentication



from flask import Flask, request
from flask_restful import Resource, Api 



#create a flask object
app = Flask(__name__)

#create an Api object
api = Api(app)



#define a HelloWorld resource class that inherits from the Resource class
class HelloWorld(Resource):

	def get(self):
		#return a message in json format
		return {'message':'hi'}

	def post(self):
		#extract the content of the request and assign it to an object
		message = request.get_json()

		#return message in json format
		return {'you sent the following message:':message}, 201



#define a Multiply resource class that inherits from the Resource class
class Multiply(Resource):

	def get(self, number):
		#return (number*78) # WRONG. FORMAT SHOULD BE JSON
		return {'result':number*78}



#add your resources and their routes to your api
api.add_resource(HelloWorld, '/')
api.add_resource(Multiply, '/multiply/<int:number>')



#run in debug mode
if __name__=='__main__':
	app.run(debug=True, port=8080)