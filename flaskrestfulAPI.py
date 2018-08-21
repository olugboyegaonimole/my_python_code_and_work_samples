
#import 

from flask import Flask
from flask import jsonify
from flask import request




#create a Flask object

app = Flask(__name__)




#what does this do. ANS: defines a route for your jsonify message to be displayed via a web port

@app.route('/', methods=['GET'])  #the / defines any sub-folders if any
def test():   #what method is this. ANS: a method which is called when you call your app.run() method
	return jsonify({'message' : 'it works'})






people = [{'person':'boy'}, {'person':'gile'}]

@app.route('/items', methods=['GET'] )
def mystuff():
	return jsonify({'people' : people})





@app.route('/items/<string:argument>', methods=['GET'])
def myperson(argument):
	personalpeople = [i for i in people if i['person']==argument]
	return jsonify({'people': personalpeople})





#run your Flask object in debug mode

if __name__=='__main__':
	app.run(debug=True, port=8080)
