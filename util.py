import smtplib
import email.message

def enviar_email():  
    corpo_email = """
    <p>Olá, segue o código de verificação</p>
    <p>Código</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = 'processonamao@gmail.com' #processonamao2802
    msg['To'] = 'wenderifpe@gmail.com'
    password = 'ukxmzkwvdokdbkiw' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')




enviar_email()