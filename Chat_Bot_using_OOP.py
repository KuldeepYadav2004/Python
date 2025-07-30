import pyttsx3 as tts
import speech_recognition as sr
import datetime as dt

class ChatBot:
    def __init__(self):
        self.name = "Ether"
        
        current_hour = dt.datetime.now().hour
        
        if current_hour < 12:
            greet = "Good morning, Sir"
        elif current_hour < 15:
            greet = "Good afternoon, Sir"
        else:
            greet = "Good evening, Sir"
            
        self.text_to_voice(greet)
            
    def text_to_voice(self, text):
        print(f"{self.name} said: {text}")

        voice_engine = tts.init() #Creating the voice enngine
        voice_engine.say(text) #Giving the text to voice enngine
        voice_engine.runAndWait() #Telling to speak the text and wait till finish    
        
    def voice_to_text(self):
        r = sr.Recognizer() #Creating the recognizer to recognize voice

        with sr.Microphone() as m: #Starting the microphone to record the voice
            print("Speak something, I am listening")

            voice = r.listen(m) #Recognizing the voice from microphone recording

        try:
            text = r.recognize_google(voice) #Coverting the voice into text using google speech recognition
            return text
        except sr.UnknownValueError:
            return None
        
    def query_to_response(self, query):
        if query.lower() in ('hello', 'helo'):
            response = "Hello, Sir"
            return response
        elif query.lower() in ('what is your name', 'what ise your name', "what's your name", "whats your name"):
            response = f"My name is {self.name}, Sir"
            return response
        elif query.lower() in ('who are you', 'hu r u'):
            response = "I am your chat bot, Sir"
            return response
        elif query.lower() in ('how are you', 'how r u'):
            response = "I am fine thank you. What about you, Sir"
            return response
        elif query.lower() in ('who created you', 'who developed you'):
            response = "I am developed by, Praveen Sir"
            return response
        elif query.lower() == 'stop' or query.lower() == 'exit' or query.lower() == 'quit':
            response = "I am leaving now, Sir"
            return response
        else:
            response = "I do not know about it, Sir"
            return response

chat_bot = ChatBot()

while True:
    query = chat_bot.voice_to_text()
    
    if query is not None:
        response = chat_bot.query_to_response(query)
        if response == "I am leaving now, Sir":
            print(f"You asked: {query}")
            chat_bot.text_to_voice(response)
            break
        else:
            print(f"You asked: {query}")
            chat_bot.text_to_voice(response)
    else:
        chat_bot.text_to_voice("Sorry sir, I did not understand what you said")
    
        