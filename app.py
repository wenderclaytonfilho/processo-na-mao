from flask import *
from util import *


app = Flask(__name__)
@app.route("/", methods=['GET','POST'])
def buscar_processo(name=None):
  if request.method == 'POST':
    codigoGerado = gerar_codigo()
    email = request.form.get('email')
    numero_do_processo = request.form.get('numeroprocesso')
    get_processo_por_numero(numero_do_processo)
    enviar_email(email,codigoGerado)
    return redirect(url_for('confirmar'))
  return render_template('index.html',name=name)

@app.route("/confirmar", methods=['GET','POST'])
def confirmar(name=None):
  codigoInserido = request.form.get('codigodeconfirmacao')
  if request.method == 'POST':
    verificar_codigo(codigoInserido)
  return render_template('confirm.html',name=name)

@app.route("/sucesso", methods=['GET'])
def sucesso(name = None):
  return "<p>Sucesso na operação!</p>"



if __name__=="__main__":
  app.run(debug=True,port=10)