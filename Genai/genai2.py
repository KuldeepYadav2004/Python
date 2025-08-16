import speech_recognition as sr
import google.generativeai as genai
import pyttsx3
import os

# Configure Gemini API (ensure GEMINI_API_KEY is set as an environment variable)
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# Initialize speech recognizer and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_for_command():
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def main():
    wake_word = "gemini"
    exit_words = ["exit", "stop", "quit", "bye", "goodbye"]

    while True:
        with sr.Microphone() as source:
            print(f"Say '{wake_word}' to activate...")
            audio = r.listen(source)
        try:
            activation_phrase = r.recognize_google(audio).lower()
            if wake_word in activation_phrase:
                speak("Hello, how can I help you?")
                while True:
                    command = listen_for_command()
                    if any(word in command for word in exit_words):
                        speak("Goodbye!")
                        break
                    if command:
                        try:
                            # Send command to Gemini API
                            model = genai.GenerativeModel('gemini-pro')
                            response = model.generate_content(command)
                            speak(response.text)
                        except Exception as e:
                            print(f"Error interacting with Gemini API: {e}")
                            speak("I encountered an error. Please try again.")
        except sr.UnknownValueError:
            pass # Continue listening if no clear activation phrase
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    main()