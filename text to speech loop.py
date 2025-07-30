import pyttsx3 as tts
text='welcome to incapp'

print(text)
engine = tts.init()
engine.say(text)
engine.runAndWait()
