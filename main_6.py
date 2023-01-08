"""
#############################################################################
TOPIC :
1. path variables in URL
2. using path variables in function (view)
3. The path variables rules can be found here -
https://flask.palletsprojects.com/en/2.2.x/quickstart/#variable-rules

#############################################################################

flask --app main4 run


NOTE -
If you rename file name as either `app.py` OR `wsgi.py`,
you can directly use `flask run` in terminator


1. PATH variable

example -
    <home-url>/addition/num1/num2
    here, num1 and num2 are path variables
below are the converters
    string:
    int:
    float:
    path:
    uuid:

2. query parameter
"""

from flask import Flask

app = Flask(__name__)  # initiating  flask

@app.route('/')
def hello():
    return '<h1> hellow world </h1>'


# syntax: @app.route('/relative path/<converter:parameter_name>/<converter:parameter_name>')
@app.route('/addition/<int:num1>/<int:num2>')
def _add(num1, num2):
    result = num1 + num2
    return f'<h1> {result} </h1>'


@app.route("/about/<institute>")
def about(institute):
    print(type(institute))
    return f"<h1> handcrafted by Prashant - {institute}</h1>"


if __name__ == '__main__':
    app.run(host='localhost', port=8080)

# http://localhost:8080/addition/20/30 to check addition url data on server.
# need to pass argument of funtion in url