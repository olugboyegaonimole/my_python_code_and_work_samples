from flask import Flask, request, jsonify


# create flask object

app = Flask(__name__)




# pull data from a database via a database connection, or, create data to be displayed

mylist1 = ['jon', 'jen', 'jin']


mylist2 = [{'name':'jik'}, {'name':'jeck'}, {'name':'jack'}] # each item in this list is a dictionary




# create uri endpoint (to respond to a GET request from a client?)

@app.route('/') # this is a route on the index that returns a message in json form
def myfunction1(): # this endpoint function must be a unique function
	return jsonify({'message':'hello world it works test'})




# create uri endpoint 2 (to respond to a GET request from a client?)

@app.route('/mylist1', methods=['GET'])
def myfunction2(): # this endpoint function must be a unique function
	return jsonify({'message':mylist1})




# create uri endpoint 3 (to respond to a GET request from a client?)

@app.route('/message2', methods=['GET'])
def myfunction3(): # this endpoint function must be a unique function
	return jsonify({'message':mylist2})




# run in debug mode

if __name__=='__main__':
	app.run(debug=True, port=8080)