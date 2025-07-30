import datetime as dt
import pyttsx3 as tts
import speech_recognition as sr

assistant_name = "Ether" 

def text_to_voice(text):
    print(f"{assistant_name} said: {text}.")

    voice_engine = tts.init()
    voice_engine.say(text)
    voice_engine.runAndWait()

def voice_to_text():
    r = sr.Recognizer() #Creating the speech recongnizer

    with sr.Microphone() as m: #Starting the microphone to record the voice
        text = "Ask me something, I am listening"
        text_to_voice(text)

        voice = r.listen(m) #It is converting the recording into voice

    try:
        text = r.recognize_google(voice) #It is converting voice into text
        return text
    except Exception:
        return None

current_hour = dt.datetime.now().hour

if current_hour < 12:
    text = "Good morning, Sir"
elif current_hour < 18:
    text = "Good afternoon, Sir"
elif current_hour < 22:
    text = "Good evening, Sir"
else:
    text = "Good night, Sir"

text_to_voice(text)

while True:
    query = voice_to_text()
    
    if query is not None:
        if query.lower() in ('what is your name', 'what ise your name', 'whats your name', "what's your name"):
            print(f"You asked: {query}")
            answer = "My name is " + assistant_name
            text_to_voice(answer)
        elif query.lower() in ('who are you', 'hu r u'):
            print(f"You asked: {query}")
            answer = "I am your virtual assistant"
            text_to_voice(answer)
        elif query.lower() in ('how are you', 'how r u'):
            print(f"You asked: {query}")
            answer = "I am fine thank you. What about you, Sir"
            text_to_voice(answer)
        elif query.lower() == 'stop' or text.lower() == 'exit' or text.lower() == 'quit':
            text_to_voice("I am leaving now, Sir")
            break
        else:
            answer = "I do not know about it, Sir"
            text_to_voice(answer)
    else:
        text = "Sorry!, I did not undersatand what you said"
        text_to_voice(text)
