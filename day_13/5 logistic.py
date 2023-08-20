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
        print("Listeing")
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
    hora=(F"Right now is {hora.hour} hours with {hora.minute} minutes")
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


def pedir_cosas():
    saludo_inicial()

    comenzar=True

    while comenzar:
        pedido=transformar_audio_en_texto().lower()

        if 'open youtube' in pedido:
            hablar('Sure i am opening youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'open explorer' in pedido:
            hablar('Sure i am opening the explorer')
            webbrowser.open('https://www.google.com')
            continue
        elif 'open instagram' in pedido:
            hablar('Sure i am opening instagram')
            webbrowser.open('https://www.instagram.com')
            continue
        elif 'open linkedin' in pedido:
            hablar('Sure i am opening linkedin')
            webbrowser.open('https://www.linkedin.com')
            continue
        # elif 'todays date':
        #     pedir_dia()
        #     continue
        # elif 'what time is it?':
            pedir_hora()
            continue
        elif 'wikipedia' in pedido:
            hablar('Sure i am searching in wikipedia')
            resultado=wikipedia.summary(pedido,sentences=3)
            hablar('According to wikipedia')
            hablar(resultado)
            continue
        elif 'reproduce' in pedido:
            hablar('Sure i reproducing in youtube')
            pywhatkit.playonyt(pedido)
            continue
        elif 'see you tomorrow' in pedido:
            hablar('See you soon!!')
            break

pedir_cosas()




    

