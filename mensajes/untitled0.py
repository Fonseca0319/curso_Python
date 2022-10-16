# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 18:54:46 2022

@author: Usuario
"""
from flask import Flask 
import os
from twilio.rest import Client
from flask import request

app = Flask(__name__)

@app.route("/")
def inicio():
    test= os.environ.get("Test")
    return test

@app.route("/sms")
def sms():
    try:
    
        # Find your Account SID and Auth Token at twilio.com/console
        # and set the environment variables. See http://twil.io/secure
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)
        contenido = request-args.get("mensaje")
        destino = request.args.get("telefono")
        message = client.messages \
                        .create(
                             body=contenido,
                             from_='+12284006572',
                             to='+57' + destino
                         )
        
        print(message.sid)
        return "Enviado Correctamente"
        
    except Exception as e:
        return "Error enviando el mensaje"
        

    

if __name__ == '__main__':
    app.run()
    