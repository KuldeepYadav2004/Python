import pyttsx3 #Importing the text to speech library
text='Hello INCAPP'
print(text)
texttospeechconvertor=pyttsx3.init() #Creating a text to speech convertor
texttospeechconvertor.say(text) #Tell the text that to  converted into speech
texttospeechconvertor.runAndWait() #will speak the text and wait to finish


