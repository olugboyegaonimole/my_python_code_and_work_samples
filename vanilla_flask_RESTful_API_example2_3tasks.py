# BUILD A REST API USING PYTHON AND VANILLA FLASK



# TASK 1: BUILD A BASIC WEB APPLICATION WITH FLASK

# TASK 2: BUILD A REST API USING PYTHON AND FLASK (INDEX FOLDER ONLY, GET METHOD ONLY)

# TASK 3: BUILD A REST API USING PYTHON AND FLASK (INDEX FOLDER AND ADDITIONAL SUB FOLDERS, GET AND POST METHODS)



# what is flask?

# a micro framework for building web applications

  # very basic framework

  # simple set of components - can be extended 

  # elegance and simplicity

  # comes with several extensions eg RESTful?
  




# TASK 1: BUILD A BASIC WEB APPLICATION WITH FLASK


from flask import Flask



#create Flask object

app = Flask(__name__)





#create URI ENDPOINT #is this a URI endpoint?

@app.route('/') # the decorator converts the function hello() to a URI endpoint
def hello():
  return "hello TESTING"





#run in debug mode

if __name__=='__main__':
  app.run(debug=True, port=8080)







# TASK 2: BUILD A REST API USING PYTHON AND FLASK (ROOT FOLDER ONLY, GET METHOD ONLY)

#EXAMPLE 1

from flask import Flask, jsonify



#create Flask object

app = Flask(__name__)





#create URI ENDPOINT

@app.route('/') # the decorator converts the function hello() to a URI endpoint
def hello():
  return jsonify({'message':"hello TESTING"}) # the jsonified output converts the web app to a REST API





#run in debug mode

if __name__=='__main__':
  app.run(debug=True, port=8080)





# TASK 3: BUILD A REST API USING PYTHON AND FLASK VANILLA (ROOT FOLDER AND ADDITIONAL SUB FOLDERS, GET AND POST METHODS)

from flask import Flask, jsonify, request


# here you can

	#have more routes
	#have more parameters as input to the URI
	#have other (works?) HTTP methods

#response codes

	#default for a GET request is 200



app =  Flask(__name__)




@app.route('/multiply/<int:number>', methods=['GET', 'POST']) # this endpoint accepts values that you can process further
def myfunction(number):
	return jsonify({'result':number * 89})




#this URI endpoint will work both with GET requests and with POST requests as well
@app.route('/', methods=['GET', 'POST'])
def myfunction2():

	#check the request type
	if request.method=='POST':

		#extract the content of the request
		message = request.get_json()

		#send the content back in the response
		return jsonify({'you sent this':message}), 201

	else:
		return jsonify({'message':'this is a GET request'})


if __name__=='__main__':
	app.run(debug=True, port=8080)





