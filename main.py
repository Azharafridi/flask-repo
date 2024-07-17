## integrating HTML with flask
### HTTP Verb GET AND POST

from flask import Flask, redirect, url_for, render_template, request


# WSGI application
app = Flask(__name__)

# This is the decorator
@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res = ''
    if score <=49:
        res = 'Failed'
    else:
        res = 'Passed'
    return render_template('result.html', result = res)


@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed and the marks is " + str(score)

## result checker
@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks < 50:
        result = 'fail'
    else:
        result = 'success'
    return redirect(url_for(result,score=marks))

## result checker html page
@app.route('/submit', methods = ['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['Science'])
        maths = float(request.form['Maths'])
        english = float(request.form['English'])
        urdu = float(request.form['urdu'])
        total_score = (science+maths + english + urdu)/4
    res = ''
    return redirect(url_for('success', score = total_score))
    

if __name__ == '__main__':
    app.run(debug=True)
