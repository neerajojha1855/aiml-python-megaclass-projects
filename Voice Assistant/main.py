import pyttsx3
import wikipedia
import pyaudio
import speech_recognition as sr
from datetime import datetime

# Set Wikipedia User-Agent to avoid getting blocked (which causes the JSONDecodeError)
wikipedia.set_user_agent("MyVoiceAssistant/1.0 (contact@example.com)")

def speak(text):
    # Re-initialize the engine per utterance to avoid SAPI5 audio deadlocks in while loop
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    if voices:
        engine.setProperty('voice', voices[0].id)
    engine.setProperty('volume', 1.0)
    
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def get_time():
    time = datetime.now().strftime("%I:%M %p")

    print(f"The current time is: {time}")
    speak(f"The current time is: {time}")

def search_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=10)
        print(result)
        speak(result)

    except wikipedia.exceptions.DisambiguationError:
        speak("There are multiple results. Please specify!")
    except wikipedia.exceptions.PageError:
        speak("No results found!")
    except Exception as e:
        speak("Sorry, I encountered an error while searching Wikipedia.")
        print(f"Wikipedia search error: {e}")

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio)
        print(f"User said: {text}")

        return text.lower()
    
    except sr.UnknownValueError:
        print("Could not understand")

        return None
    
    except sr.RequestError:
        print("Could not connect to Google Speech Recognition")

        return None

def process_command(command):
    if "time" in command:
        get_time()
    elif "wikipedia" in command:
        # Try to extract the topic from the command directly
        query = command.replace("wikipedia", "").replace("search", "").replace("on", "").replace("for", "").strip()
        filler_words = ["could", "you", "please", "can", "tell", "me", "about"]
        words = query.split()
        filtered_words = [w for w in words if w not in filler_words]
        query = " ".join(filtered_words).strip()

        if query:
            search_wikipedia(query)
        else:
            speak("What do you want to search on wikipedia?")
            new_query = recognize_speech()
            if new_query:
                search_wikipedia(new_query)
    elif "stop" in command or "exit" in command:
        speak("Thanks for you time. Love you and take care")
        exit()
    else:
        speak("Sorry, I don't understand that command. Could you please repeat")

def start_voice_assistant():
    speak("Hello! I am FRIDAY, your personal voice assistant. How can I help you?")

    while True:
        command = recognize_speech()
        if command:
            process_command(command)

if __name__ == "__main__":
    start_voice_assistant()