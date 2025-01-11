import pyttsx3
import speech_recognition as sr  # pip install SpeechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib

# Initialize the speech engine
engine = pyttsx3.init()  # Explicitly using 'espeak' for Linux
engine.setProperty('rate', 100)  # Adjust speed (100-200 recommended)
engine.setProperty('volume', 1.0)  # Max volume (range: 0.0 to 1.0)

# Set the voice for 'espeak'
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Adjust the index to select a different voice


def speak(audio):
    """Converts text to speech."""
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    """Greets the user based on the time of day."""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am your assistant. How can I help you today?")


def take_command():
    """Takes microphone input and returns it as a string."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            speak("I couldn't hear you. Please try again.")
            return "None"

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand. Please say it again.")
        return "None"
    except sr.RequestError as e:
        print(f"Google Speech Recognition service error: {e}")
        return "None"

    return query.lower()


def send_email(to, content):
    """Sends an email using SMTP."""
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("your-email@gmail.com", "your-app-password")  # Replace with your credentials
        server.sendmail("your-email@gmail.com", to, content)
        server.quit()
        speak("Email has been sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
        speak("Sorry, I couldn't send the email.")


if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command()

        if query == "none":
            continue

        # Wikipedia Search
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                print(f"Wikipedia error: {e}")
                speak("Sorry, I couldn't find any results.")

        # Open Websites
        elif 'open youtube' in query:
            speak("Opening YouTube...")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google...")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Opening Stack Overflow...")
            webbrowser.open("stackoverflow.com")

        # Play Music
        elif 'play music' in query:
            music_dir = "/path/to/your/music"  # Update this with the correct directory
            try:
                songs = os.listdir(music_dir)
                if songs:
                    os.startfile(os.path.join(music_dir, songs[0]))
                    speak("Playing music...")
                else:
                    speak("No songs found in the music directory.")
            except FileNotFoundError:
                speak("Music directory not found. Please check the path.")

        # Tell Time
        elif 'the time' in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {current_time}")

        # Send Email
        elif 'email to' in query:
            try:
                speak("What should I say?")
                content = take_command()
                if content == "none":
                    speak("Email content not provided.")
                    continue
                recipient_email = "recipient@example.com"  # Replace with the recipient's email
                send_email(recipient_email, content)
            except Exception as e:
                print(f"Error: {e}")
                speak("Sorry, I couldn't send the email.")


