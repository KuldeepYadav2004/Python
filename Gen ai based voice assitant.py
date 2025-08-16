#Importing the required library
import pyttsx3 as tts
import speech_recognition as sr
import datetime as dt
import google.genai as genai


class VoiceAssistant:
    def __init__(self, name = "Ether"):
        self.name = name
        self.client = genai.client(api_key=AIzaSyCh87E6GisHYTFDz4wydzh4gvHd_KY5AvE)
        
        current_hour = dt.datetime.now().hour
        
        if current_hour < 12:
            greet = "Good morning, Sir"
        elif current_hour < 17:
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
            print("I am listening, Ask me")

            voice = r.listen(m) #Recognizing the voice from microphone recording

        try:
            text = r.recognize_google(voice) #Coverting the voice into text using google speech recognition
            return text
        except sr.UnknownValueError:
            return None
        
    def query_to_response(self, query):
        query = query.lower()
        if query in ('hello', 'helo'):
            response = "Hello, Sir"
        elif query in ('what is your name', 'what ise your name', "what's your name", "whats your name"):
            response = f"My name is {self.name}, Sir"
        elif query in ('who are you', 'hu r u'):
            response = "I am your voice assistant, Sir"
        elif query in ('how are you', 'how r u'):
            response = "I am fine thank you. What about you, Sir"
        elif query in ('who created you', 'who developed you'):
            response = "I am developed by, Praveen Sir"
        elif query == 'stop' or query.lower() == 'exit' or query.lower() == 'quit':
            response = "I am leaving now, Sir"
        elif 'what' in query or 'why' in query or 'when' in query or 'tell' in query or 'who' in query or 'how' in query:
            response = self.client.models.generate_content_stream(model='gemini-2.5-flash', contents=query + " and keep it short")
            is_ai_generated = True
            is_long_answer = False
            return response, is_ai_generated, is_long_answer
        elif 'write' in query or 'create' in query or 'generate' in query:
            response = self.client.models.generate_content_stream(model='gemini-2.5-flash', contents=query)
            is_ai_generated = True
            is_long_answer = True
            return response, is_ai_generated, is_long_answer
        else:
            response = "I do not know about it, Sir"
        is_ai_generated = False
        is_long_answer = False
        return response, is_ai_generated, is_long_answer

voice_assistant = VoiceAssistant()

while True:
    query = voice_assistant.voice_to_text()
    
    if query is not None:
        response, is_ai_generated, is_long_answer = voice_assistant.query_to_response(query)
        
        if response == "I am leaving now, Sir":
            print(f"You asked: {query}")
            voice_assistant.text_to_voice(response)
            break
        elif response and is_ai_generated and not is_long_answer:
            print(f"You asked: {query}")
            for line in response:
                line = line.text
                line = line.replace("*", "")
                line = line.replace("#", "")
                voice_assistant.text_to_voice(line)
        elif response and is_ai_generated and is_long_answer:
            print(f"You asked: {query}")
            voice_assistant.text_to_voice("Please wait, I am getting your answer")
            for line in response:
                line = line.text
                line = line.replace("*", "")
                line = line.replace("#", "")
                print(line)
            voice_assistant.text_to_voice("End of your answer")
        elif response and not is_ai_generated:
            print(f"You asked: {query}")
            voice_assistant.text_to_voice(response)
        else:
            print(f"You asked: {query}")
            voice_assistant.text_to_voice(response)
    else:
        voice_assistant.text_to_voice("Sorry sir, I did not understand what you said")
    
        
