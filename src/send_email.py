"""
Uso: Envío de correos con datos adjuntos
Creado: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 03 Mayo 2020
"""

import email, smtplib, ssl
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from os.path import basename
from datetime import datetime
import os

def main():
    os.system("cls")
    print(datetime.now(), "\033[0;32m [INFO] Envío de correos con datos adjuntos \033[0;0m")
    print(datetime.now(), "\033[0;32m [INFO] Iniciar sesión ... \033[0;0m \n")
    #test.pc.fcfm@gmail.com
    #fcfm.123
    while(True):        
        sender_email = input("From > ")    
        password = getpass.getpass("Password > ")
        if not sender_email or not password:
            os.system("cls")
            print(datetime.now(), "\033[0;31m [INFO] Iniciar sesión \033[0;0m")
            print(datetime.now(), "\033[0;31m [INFO] From y password son datos obligatorios \033[0;0m \n")
        else:
            break        
    receiver_email = input("To > ")
    #andreshernandezmta@gmail.com    
    #eb5fc07b.uanl.edu.mx@amer.teams.ms
    subject = input("Subject > ")
    #Envío de correos con datos adjuntos
    body = input("Body > ")
    #Esta es una prueba
    image = input("Imagen > ")

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
       
    html = """\
    <html>
    <head></head>
    <body>
        <img src="cid:image"><br>        
    </body>
    </html>
    """    
    msgHtml = MIMEText(html, 'html')

    img = open("seguro-de-vida.png", 'rb').read()
    msgImage = MIMEImage(img, 'png')
    msgImage.add_header('Content-ID', '<image>')
    msgImage.add_header('Content-Disposition', 'inline', filename="seguros-de-vida.png")
      
    message.attach(MIMEText(body,"plain"))
    message.attach(msgHtml)
    message.attach(msgImage)

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)        
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    except Exception as error:
        print(error)
    finally:        
        server.quit()

if __name__ == '__main__':
    main()