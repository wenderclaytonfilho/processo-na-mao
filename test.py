from flask import *

app = Flask(__name__)

@app.route("/")
def index(name=None):
  return render_template('index.html',name=name)


app.run()