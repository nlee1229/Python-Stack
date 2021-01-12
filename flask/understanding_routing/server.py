from flask import Flask, render_template
app = Flask(__name__)    


@app.route('/<name>')  
def index(name):
    print(name)
    return render_template('index.html', name_on_template = name)  

@app.route('/hello')
def hello():
    return "Hello!"

@app.route('/hello/<num>')  #num is just a namee of a variable 
def say_hello(num):
    print("Hello from my function!", num)
    return "Hello " * int(num)  

if __name__=="__main__":    
    app.run(debug=True)   


