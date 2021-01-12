#hello assignemnt lecture video walkthrough

from flask import Flask
app = Flask(__name__)    


@app.route('/')  
def index():
    return "I am awesome!"

@app.route('/hello')
def hello():
    return "Hello!"

@app.route('/hello/<num>')  #num is just a namee of a variable 
def say_hello(num):
    print("Hello from my function!", num)
    return "Hello " * int(num)  

if __name__=="__main__":    
    app.run(debug=True)   

