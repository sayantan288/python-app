from flask import Flask, request
import sqlite3
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, Tails.com!'
@app.route('/wag/', methods=['POST'])
def wag():
    command = request.form['command']
    dATABASE = sqlite3.connect('wag_or_not.sqlite')
    c = dATABASE.cursor()


    c.execute("SELECT wag FROM wag_or_not WHERE command='" + command + "'")
    has_it_had_a_wag_or_dit_it_not = c.fetchone()[0]

    if has_it_had_a_wag_or_dit_it_not == 1:
          return '{"wag": true}'
    else:
        return '{"wag": false}'
