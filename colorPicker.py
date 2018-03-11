# Dev: Michael G.
# Date: 3/10/2018
# Description:
# Simple app that renders different colors from user input

from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    print session['colors']
    if 'colors' in session:
        print session['colors']         
        rgb = session['colors']
    else:
        rgb = "rgb(0,0,0)"
    return render_template("index.html", color=rgb)

@app.route('/colors', methods=['POST'])
def getColors():
    # get colors from form input
    redColor = request.form['redVal']
    greenColor = request.form['greenVal']
    blueColor = request.form['blueVal']

    # concatenate the new color and store in sessions
    session['colors'] = "rgb("+ redColor + ',' + greenColor + ',' + blueColor + ")"
    return redirect('/')

app.run(debug=True)
