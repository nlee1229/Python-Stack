from flask import Flask, render_template
app = Flask(__name__)    

@app.route('/play/<int:num>') 
def lets_play(num): 

    return render_template('playground.html', num_of_boxes = num) 

@app.route('/play/<int:num>/<color>') 
def lets_play_with_color(num,color): 

    return render_template('playground.html', num_of_boxes = num, box_color = color) 
    #differentiates the variable from the value
    

if __name__=="__main__":    
    app.run(debug=True)  