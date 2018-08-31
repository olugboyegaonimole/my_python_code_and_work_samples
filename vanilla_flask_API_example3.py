from flask import Flask, request, jsonify


# create flask object

app = Flask(__name__)




# obtain data via a database connection or create data to be displayed

mylist1 = ['jon', 'jen', 'jin']


mylist2 = [{'name':'jik'}, {'name':'jeck'}, {'name':'jack'}] # each item in this list is a dictionary




# create uri endpoint

@app.route('/')
def myfunction1(): # endpoint function must be a unique function
	return jsonify({'message':'hello world it works test'})




# create uri endpoint 2

@app.route('/mylist1', methods=['GET'])
def myfunction2(): # endpoint function must be a unique function
	return jsonify({'message':mylist1})




# create uri endpoint 3

@app.route('/message2', methods=['GET'])
def myfunction3(): # endpoint function must be a unique function
	return jsonify({'message':mylist2})




# run in debug mode

if __name__=='__main__':
	app.run(debug=True, port=8080)