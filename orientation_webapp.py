from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    
    return "Hello World"


@app.route("/babylon_orientation")
def get_oriention():
    
    return render_template("orient_canvas.html")


if __name__ == '__main__':

    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)
