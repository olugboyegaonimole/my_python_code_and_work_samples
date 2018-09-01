from flask import Flask, request, jsonify


# create flask object

app = Flask(__name__)




# pull data from your database via a database connection, or, create a database? to be returned to your user

mylist1 = [{'name':'jakson'}, {'name':'jik'}, {'name':'jok'}, {'name':'jebo'}, {'name':'jek'}]





# create uri/api endpoint 1 (a route on the index) responds to a GET request (by default) and returns a hard coded message

@app.route('/')
def myfunction1():
	return jsonify({'message':'it works test'})





# create uri/api endpoint 2 (the 'mylist1' endpoint) responds to a GET request and returns the entire database

@app.route('/mylist1', methods=['GET']) # this route is created to respond only to GET requests
def myfunction2():
	return jsonify({'database':mylist1})





# create uri/api endpoint 3 to respond to a GET request and return only part of the database
# to search through the database by the key 'name' and return the dictionary associated with the value specified as a search parameter

@app.route('/mylist1/<string:argument>', methods=['GET']) # a route with a parameter 'argument' in it
def myfunction3(argument):
	result_list = [i for i in mylist1 if i['name']==argument]
	return jsonify({'result':result_list[0]})





# create uri/api endpoint 4 to POST to the database via route 'mylist1'
# POSTMAN will be used to send POST requests to this api endpoint because it will not be possible to use the browser to send the requests easily

@app.route('/mylist1', methods=['POST']) # this POST request will not update or insert into the database, rather it will only append to the database
def  myfunction4():
	
	# from POSTMAN post a dictionary using a POST request in the format {"property name":"value"} replicate the double quotes
	# make sure to use the uri above as your request uri
	# then go to the 'Body' tab, select 'raw' as your entry format, and enter your data as a json object
	# the dictionary you send with the post request must have the same form as the dictionary in your database
	

	# myfriends = {'name': request.json['name']} #failed #attempted to create a dictionary where the key is 'name' (identical to the key used in your database) and the value is the value extracted from the json that was sent with the POST request


	myfriends = request.get_json('anything') #successful #this gets the entire dictionary posted by the user
	# IT DOES NOT MATTER WHAT STRING YOU PASS AS ARGUMENT TO THE get_json() METHOD ABOVE


	# append this new dictionary to the list in the database
	mylist1.append(myfriends)


	#return everything
	return jsonify({'new database':mylist1})





# create uri endpoint 5 to respond to PUT requests

# in POSTMAN, first run a GET request on your database: take the value of the dictionary in the database that you wish to update and use it as the sub-folder parameter of your GET request
# select PUT as your method and use the uri above as your request url
# then go to the 'Body' tab, select 'raw' as your entry format, enter your data as a json object and send

@app.route('/mylist1/<string:argument>', methods=['PUT'])
def myfunction5(argument):

	# find the dictionary that matched the name requested by the user
	result_list = [i for i in mylist1 if i['name']==argument]


	# receive the json PUT by the user
	user_input = request.get_json('anything')


	# equate the value of the search result to the value of the user input
	result_list[0]['name'] = user_input['name']


	return jsonify({'new database': result_list[0]})




# create uri endpoint 6 to respond to delete requests

@app.route('/mylist1/<string:argument>', methods=['DELETE'])
def myfunction6(argument):

	#find
	result_list = [i for i in mylist1 if i['name']==argument]

	
	#remove the first result
	mylist1.remove(result_list[0])


	return jsonify({'new database': mylist1})




# run in debug mode

if __name__=='__main__':
	app.run(debug=True, port=8080)





