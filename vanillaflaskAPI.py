# BUILD A REST API USING PYTHON AND VANILLA FLASK



# INTRODUCTION: BUILD A BASIC FLASK WEB APPLICATION

# MAIN TASK: BUILD A REST API USING PYTHON AND VANILLA FLASK



# what is flask?

# a micro framework for building web applications

  # very basic framework

  # simple set of components - can be extended 

  # elegance and simplicity

  # comes with several extensions eg RESTful?
  




# INTRODUCTION: BUILD A BASIC FLASK WEB APPLICATION


from flask import Flask


#create Flask object
app = Flask(__name__)


#create URI ENDPOINT?
@app.route('/')
def hello():
  return "hello TESTING"


#run in debug mode
if __name__=='__main__':
  app.run(debug=True, port=8080)







# MAIN TASK: BUILD A REST API USING PYTHON AND VANILLA FLASK

#EXAMPLE 1

from flask import Flask, jsonify


#create Flask object
app = Flask(__name__)


#create URI ENDPOINT
@app.route('/') # decorating with this route converts the function hello() to a URI
def hello():
  return jsonify({'message':"hello TESTING"}) # the json format converts the web app to a REST API


#run in debug mode
if __name__=='__main__':
  app.run(debug=True, port=8080)





#EXAMPLE 2

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





