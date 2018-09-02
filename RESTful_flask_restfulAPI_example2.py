#malfunctioining
#after posting new data to the database, the get method on uri '/data/<string:argument>' began to fail. Investigate

#investigation revealed that the get request failed because the new data had been posted using a key 'fish' that was different from the 

from flask import Flask, request
#from flask_restful import Resources, Api #WRONG, Resource not Resources
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)




database = [{'name':'jak'}, {'name':'jik'}, {'name':'jek'}, {'name':'jok'}, {'name':'jukun'}]




class Get1(Resource):

	def get(self): # responds to every get request sent to the index directory

		# return the database
		# return everything you have at index level of the database
		return {'database': database}




class Get2(Resource):

	def get(self, argument): # responds to every get request sent to the index directory with search parameter 'argument'

		# the user searches the database for a string value by going to the url and appending the string to the domain name
		# search the database values for the appended string and create a list of results
		result_list = [i for i in database if i['name']==argument]
		
		# return the list of results
		return {'result is':result_list[0]}




class Post(Resource):

	def post(self):
				
		# the user posts data to the database
		# extract this data using the get_json() method and assign it to an object
		user_post = request.get_json('some_string') # an argument must be specified for get_json otherwise a null entry is posted to the database
		
		# append the object to the database
		database.append(user_post)
		
		# return the new database
		return {'new database': database}




class Put(Resource):

	def put(self, argument):

		# the user searches the database for a string value by appending the string to the domain name (in the url)
		# search the database values for the appended string and create a result list
		result_list = [i for i in database if i['name']==argument]

		# the user posts some data to the database
		# extract the data using the get_json() method and assign it to an object
		user_post = request.get_json('some_string')

		# assign the value of the data posted by the user to the value of the result featched from the database
		result_list[0]['name'] = user_post['name']

		# return the new database
		return {'new database':database}




class Delete(Resource):

	def delete(self, argument):

		# the user searches the database for a string value by appending the string to the domain name (in the url)
		# search the database values for the appended string and create a list of results
		result_list=[i for i in database if i['name']==argument]

		# remove the result from the database
		database.remove(result_list[0])

		# return the new database
		return {'new database': database}




# if you don't add your resources to your api's you get the error message 'the method is not allowed for the requested url'

# is this the step called 'assign http methods'?

#looks like the add_resource arguments below are a http method and a URI

api.add_resource(Get1, '/data')
api.add_resource(Get2, '/data/<string:argument>')
api.add_resource(Post, '/data') 
api.add_resource(Put, '/data/<string:argument>')
api.add_resource(Delete, '/data/<string:argument>')




if __name__ =='__main__':
	app.run(debug=True, port=8080)