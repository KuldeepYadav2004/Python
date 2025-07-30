import pyttsx3 as tts
text='welcome to incapp'

print(text)
text_to_speech = tts.init()
#setting the speed of voice
text_to_speech.setProperty('rate',200)
#getting the  list of voices avialable in our computer
voices=text_to_speech.getProperty('voices')
#extracting the available voices from  voice list one by one
for voice in voices:
    #printing the voice name
    print(voice.name)

    #setting the voice for our computer
    text_to_speech.setProperty('voice',voice.id)



    text_to_speech.say(text)
    text_to_speech.runAndWait()
