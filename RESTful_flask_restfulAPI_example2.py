#malfunctioining
#review and correct


from flask import Flask, request
#from flask_restful import Resources, Api
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)



database = [{'name':'jak'}, {'name':'jik'}, {'name':'jek'}, {'name':'jok'}, {'name':'jipk'}]




class Get1(Resource):

	#def get(): #must specify self context 
	def get(self):
		return {'database':database}



class Get2(Resource):

	def get(self, argument):
		result_list = [i for i in database if i['name']==argument]
		return {'result is':result_list[0]}



class Post(Resource):

	def post(self):
		
		#dictionary = request.get_json() # an argument must be specified for get_json otherwise a null entry is posted to the database
		dictionary = request.get_json('anyting')
		
		database.append(dictionary)
		
		return {'new database': database}



class Put(Resource):

	def put(self, argument):

		result_list = [i for i in database if i['name']==argument]

		message = request.get_json('sometin')

		result_list[0]['name'] = message['name']

		return {'new database':database}



class Delete(Resource):

	def delete(self, argument):

		result_list=[i for i in database if i['name']==argument]

		database.remove(result_list[0])

		return{'new database': database}




api.add_resource(Get1, '/data')
api.add_resource(Get2, '/data/<string:argument>')
api.add_resource(Post, '/data') # otherwise 'the method is not allowed for the requested url'
api.add_resource(Put, '/data/<string:argument>')
api.add_resource(Delete, '/data/<string:argument>')




if __name__ =='__main__':
	app.run(debug=True, port=8080)