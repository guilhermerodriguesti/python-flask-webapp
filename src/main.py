import re
import os
from datetime import datetime
from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route("/branch/")
@app.route("/branch/<name>")
def branch(name=None):
    if not name:
        name = 'dev'
        os.mkdir(name)
    else:
        if not os.path.isdir(name):
            os.mkdir(name)
    return render_template("branch.html", name=name, date=datetime.now())

@app.route('/devops')
def index():
    return 'DevOps is awesome!!'

@app.route("/")
def home():
    return render_template("home.html")

# New functions
@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

app.run(host='0.0.0.0', port=8000)