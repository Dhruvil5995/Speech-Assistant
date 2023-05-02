import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listner = sr.Recognizer()
engine= pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[2].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('How can i help you sir...')
            voice = listner.listen(source)
            command= listner.recognize_google(voice)
            command = command.lower()
            if 'D' in command:
                command = command.replace('D', '')
                print(command)

    except:
        pass
    return command

def run_alexa():
    comman=take_command()
    print(comman)
    if 'play' in comman:
        song= comman.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in comman:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'tell me about ' in comman:
        person = comman.replace('tell me about', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in comman:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')

while True:
  run_alexa()




