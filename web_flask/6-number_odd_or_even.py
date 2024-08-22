#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    if n % 2 == 0:
        result = "even"
    else:
        result = "odd"
    return render_template('number.html', n=n, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

