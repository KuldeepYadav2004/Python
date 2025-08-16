import google.generativeai as genai
import speech_recognition as sr
import pyttsx3
import os

# ==== SETUP ====

# Replace with your actual API key
GEMINI_API_KEY = "AIzaSyCh87E6GisHYTFDz4wydzh4gvHd_KY5AvE"

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Text-to-speech (macOS uses 'say' or pyttsx3)
engine = pyttsx3.init()

# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to get voice input
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print("🗣️ You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand.")
        return None
    except sr.RequestError:
        print("Speech Recognition service error.")
        return None

# ==== MAIN LOOP ====
print("🧠 Gemini Voice Assistant - Say something!")

while True:
    command = listen()
    if not command:
        continue

    if "exit" in command.lower() or "quit" in command.lower():
        speak("Goodbye!")
        break

    # Send to Gemini
    try:
        response = model.generate_content(command)
        reply = response.text
        print("🤖 Gemini says:", reply)
        speak(reply)
    except Exception as e:
        print("❌ Error:", e)
        speak("Sorry, I had an error.")

