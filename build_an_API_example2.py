# what is flask?

# a micro framework for building web applications

  # basic frame work

  # simple set of components

  # elegance and simplicity
  
# basic 'hello world' flask application:


from flask import Flask



#create Flask object
app = Flask(__name__)




#create route
@app.route('/')
def hello():
  return "hello world"



#run in debug mode
if __name__=='__main__':
  app.run(debug=True)
