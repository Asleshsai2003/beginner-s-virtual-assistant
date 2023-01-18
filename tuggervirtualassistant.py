import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'tugger' in command:
                command = command.replace('tugger', '')
                print(command)
    except:
        pass
    return command


def run_tugger():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is ' in command:
        object = command.replace('who is', '')
        info = wikipedia.summary(object, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        date = datetime.datetime.now().strftime('%d / %m %Y')
        talk ('today the date is ' + date)
    elif 'are you single' in command:
        talk('yes would you mind?')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('could not get, you say again')


while True:
    run_tugger()
