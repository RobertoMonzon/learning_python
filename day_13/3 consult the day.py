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
            pedido=r.recognize_google(audio, language="es-mx")
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

    calendario={0:'Lunes',1:'Martes',2:'Miércoles',3:'Jueves',4:'Viernes',5:'Sábado',6:'Domingo'}
    hablar(f"hoy es {calendario[dia_semana]}")

pedir_dia()
    

