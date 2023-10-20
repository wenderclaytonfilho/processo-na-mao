from flask import *

app = Flask(__name__)

@app.route("/", methods=[GET,POST])
def index(name=None):
  if request.method == 'POST':
    pass
  return render_template('index.html',name=name)

@app.route("/about")
#About
def about(name=None):
  return render_template('confirm.html',name=name)


if __name__=="__main__":
  app.run(debug=True,port=10)