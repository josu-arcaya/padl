from flask import Flask, request, render_template
from jsonschema import ValidationError
from lint.utils import Padl

app = Flask(__name__)

@app.route('/')
def hello(msg=''):
    return render_template('hello.html', msg=msg, input_padl='', txt_colour='white')

@app.route('/validate', methods=['POST'])
def validate():
    #return request.form['yaml'] + "valid!"
    try:
        txt_colour = 'green'
        msg = 'Valid!'
        Padl(request.form['yaml']).validate()
    except ValidationError:
        txt_colour = 'red'
        msg = 'Not Valid'
    return render_template('hello.html', msg=msg, input_padl=request.form['yaml'], txt_colour=txt_colour)