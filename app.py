from flask import *
from util import *

app = Flask(__name__)
@app.route("/", methods=['GET','POST'])
def buscar_processo(name=None):
  if request.method == 'POST':
    codigo = gerar_codigo()
    email = request.form.get('email')
    enviar_email(email,codigo)
    return redirect(url_for('confirmar'))
  return render_template('index.html',name=name)

@app.route("/confirmar", methods=['GET','POST'])
def confirmar(name='confirmar'):
  #print(request)
  #if request.method=='POST' or request.method=='GET':
    #codigodeconfirmacao = request.form.get('codigodeconfirmacao')
    #print(codigodeconfirmacao)
    #if verificar_codigo(codigoatual,codigodeconfirmacao):
    ##print("Códigos errados")

  return render_template('confirm.html',name=name)


if __name__=="__main__":
  app.run(debug=True,port=10)