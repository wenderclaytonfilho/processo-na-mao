from flask import *
from util import *


app = Flask(__name__)
@app.route("/", methods=['GET','POST'])
def buscar_processo(name=None):
  if request.method == 'POST':
    codigoGerado = gerar_codigo()
    codigos.append(codigoGerado)
    email = request.form.get('email')
    enviar_email(email,codigoGerado)
    return redirect(url_for('confirmar'))
  return render_template('index.html',name=name)

@app.route("/confirmar", methods=['GET','POST'])
def confirmar(name=None):
  codigoInserido = request.form.get('codigodeconfirmacao')
  print(codigos)
  if request.method == 'POST':
    verificar_codigo(codigoInserido)
  return render_template('confirm.html',name=name)


if __name__=="__main__":
  app.run(debug=True,port=10)