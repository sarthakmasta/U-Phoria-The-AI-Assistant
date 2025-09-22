import speech_recognition as sr

def speech_conversion():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                voice_data = r.recognize_google(audio)
                print(voice_data)
                return voice_data
            except sr.UnknownValueError:
                print("Sorry, I couldn't hear you.")
                return "Sorry, I couldn't hear you."
            except sr.RequestError:
                print("Speech recognition service unavailable.")
                return "Speech recognition service unavailable."
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return f"Error: {e}"

