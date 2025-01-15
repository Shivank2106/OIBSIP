import pyttsx3
import wikipedia
import webbrowser
import datetime
import speech_recognition as sr
import os
# Initialize the voice engine
voice = pyttsx3.init()

# Function to respond to "Hello"
def respond_hello():
    voice.say("Hello! How can I assist you today?")
    voice.runAndWait()

# Function to tell the time
def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    voice.say("The current time is " + current_time)
    voice.runAndWait()

# Function to tell the date
def tell_date():
    current_date = datetime.datetime.now().strftime("%B %d, %Y")
    voice.say("Today's date is " + current_date)
    voice.runAndWait()

# Function to search the web
def search_web(query):
    url = "https://www.google.com/search?q=" + query
    webbrowser.open(url)

# Function to get user query
def get_query():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio)
            print("User said: " + query)
            return query
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""
        except sr.RequestError:
            print("Could not request results")
            return ""

# Main function
def main():
    while True:
        query = get_query().lower()
        if "hello" in query:
            respond_hello()
        elif "time" in query:
            tell_time()
        elif "date" in query:
            tell_date()
        elif "search" in query:
            search_web(query.replace("search", ""))
        elif "exit" in query or "quit" in query:
            voice.say("Goodbye!")
            voice.runAndWait()
            break
        else:
            try:
                result = wikipedia.summary(query, sentences=3)
                voice.say(result)
                voice.runAndWait()
            except wikipedia.exceptions.DisambiguationError:
                voice.say("Multiple pages found. Please be more specific.")
                voice.runAndWait()
            except wikipedia.exceptions.PageError:
                voice.say("Page not found. Please check your query.")
                voice.runAndWait()

if __name__ == "__main__":
    main()
