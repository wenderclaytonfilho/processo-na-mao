import smtplib
import email.message
import random
import requests
import json


api_key = 'cDZHYzlZa0JadVREZDJCendQbXY6SkJlTzNjLV9TRENyQk1RdnFKZGRQdw=='
api_url = 'https://api-publica.datajud.cnj.jus.br/api_publica_trf1/_search'

headers ={
    "Authorization": "APIKey cDZHYzlZa0JadVREZDJCendQbXY6SkJlTzNjLV9TRENyQk1RdnFKZGRQdw==",
    'Content-Type': 'application/json'
}

codigos = [

]




def get_processo_por_numero(numerodoprocesso):
    payload = json.dumps({
  "query": {
    "match": {
      "numeroProcesso": numerodoprocesso
    }
  }
})
    
    response = requests.request('POST', api_url,headers=headers,data=payload)
    dados = response.json()
    print(dados)
    


def checar_field(data):
    if not data:
        return False
    return True


def enviar_email(mail,codigo):  
    corpo_email = """
    <p>Olá, segue o código de verificação</p>
    <p>{}</p>
    """.format(codigo)

    msg = email.message.Message()
    msg['Subject'] = "Código de verificação!"
    msg['From'] = 'processonamao@gmail.com' #processonamao2802
    msg['To'] = mail
    password = 'ukxmzkwvdokdbkiw' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

def gerar_codigo():
    codigo = random.randint(0,9999)
    return codigo

def verificar_codigo(codigorecebido):
    print (codigorecebido)
    if codigorecebido in codigos:
        print("Código correto!")


def coletar_processo(numerodoprocesso):
    pass