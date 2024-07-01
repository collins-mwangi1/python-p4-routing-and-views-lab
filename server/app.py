#!/usr/bin/env python3
#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_parameter(parameter):
    return parameter

@app.route('/print_to_console/<parameter>')
def print_to_console(parameter):
    print(parameter)  # Print to console directly
    return ''

if __name__ == '__main__':
    app.run(debug=True)
