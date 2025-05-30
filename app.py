from flask import Flask, render_template
import numpy as np

app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/start')
def start():
    return render_template("start.html")

@app.route('/main')
def main():
    op = np.random.randint(1, 7)
    return render_template('main.html', op=op)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
