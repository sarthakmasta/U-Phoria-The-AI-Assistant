import pyttsx3

def AI_voice_output(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 'rate-70')
    engine.say(text)
    engine.runAndWait()