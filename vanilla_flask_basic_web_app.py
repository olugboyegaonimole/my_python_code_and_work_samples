

# what is flask?

# a micro framework for building web applications

  # very basic framework

  # simple set of components - can be extended 

  # elegance and simplicity

  # comes with several extensions eg RESTful?
  




# BUILD A BASIC WEB APPLICATION WITH FLASK


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




