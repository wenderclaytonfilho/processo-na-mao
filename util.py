import smtplib
import email.message
import random

def enviar_email(mail,codigo):  
    corpo_email = """
    <p>Olá, segue o código de verificação</p>
    <p>{}</p>
    """.format(codigo)

    msg = email.message.Message()
    msg['Subject'] = "Assunto"
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

def verificar_codigo(codigo,codigorecebido):
    if codigo == codigorecebido:
        return True
    else:
        return False