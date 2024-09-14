import os
import smtplib
from email.message import EmailMessage
from time import sleep
from emails import address, password

def enviar_email():
    #Configurar email, senha
    email_address = address
    email_password = password

    for i in range(15):
        #Envia 15 emails para a conta abaixo
        email = EmailMessage()
        email['Subject'] = f'Teste de e-mail {i}'
        email['From'] = email_address
        email['To'] = 'conta@destino.com'
        email.set_content('Corpo do email - teste de conta padrão')

        #Enviar do e-mail
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(email)

            print('Email conta padrão enviado')
        
enviar_email()
