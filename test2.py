import speech_recognition as sr

while True:
    #Creating the speech recognizer
    r = sr.Recognizer()

    with sr.Microphone() as source: #Setting microphone as the source to listen
        print("Speak something, I am listening....")

        speech = r.listen(source) #Getting the audio from microphone

    try:
        text = r.recognize_google(speech) #Coverting speech to text

        if text.lower() == 'stop' or text.lower() == 'exit' or text.lower() == 'quit':
            print("I am leaving now....")
            break
        
        print("You said:", text)
    except Exception:
        print("Sorry!, I didn't understand what you said")
