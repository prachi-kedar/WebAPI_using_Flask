import flask
from flask import render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/home/<user>')
def home(user):
    # return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"
    return render_template('index.html', name=user)


@app.route('/hello/<name>', methods=['GET'])
def hello_name(name):
    return '<h1>Hello %s</h1>' % name


@app.route('/revision/<float:revNo>', methods=['GET'])
def revision(revNo):
    return '<h1>The revision number is %f</h1>' % revNo


@app.route('/blog/<float:blogNo>', methods=['GET'])
def blogNo(blogNo):
    return '<h1>The revision number is %f</h1>' % blogNo


app.run()
