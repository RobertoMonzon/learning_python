# https://www.youtube.com/watch?v=x-BtaZDbQeo&ab_channel=TechieDude <==== in case of an error check tutorial
import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

def transformar_audio_en_texto():
    r=sr.Recognizer()
    with sr.Microphone() as origen:
        r.pause_thresholh= 0.8
        print("Habla")
        audio=r.listen(origen)

        try:
            pedido=r.recognize_google(audio, language="EN-US")
            print("Dijiste:" + pedido)
            return pedido
        
        except sr.UnknownValueError:
            print("Ups, no entendi")
            return "Sigo esperando"
        
        except sr.RequestError:
            print("Ups, no entendi")
            return "Sigo esperando"
        
        except:
            print("Ups,algo salio mal")
            return "Sigo esperando"
        
def hablar(mensaje):
    engine= pyttsx3.init()

    engine.say(mensaje)
    engine.runAndWait()


def pedir_dia():
    dia=datetime.date.today()
    print(dia)

    dia_semana=dia.weekday()
    print(dia_semana)

    calendario={0:'Monday',1:'Tusday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
    hablar(f"today is {calendario[dia_semana]}")

def pedir_hora():
    hora=datetime.datetime.now()
    hora=(F"Right now is  {hora.hour} hourss with {hora.minute} minutes")
    print(hora)

    hablar(hora)

def saludo_inicial():

    hora=datetime.datetime.now()
    if hora.hour <6 or hora.hour >20:
        momento="good night"
    elif hora.hour >= 6 and hora.hour <13:
        momento = 'Good morning'
    else:
        momento='Good afternoon'
    

    hablar(f'{momento}, I am Roberta, your personal assistant. tell me how i can help you')

saludo_inicial()



    

