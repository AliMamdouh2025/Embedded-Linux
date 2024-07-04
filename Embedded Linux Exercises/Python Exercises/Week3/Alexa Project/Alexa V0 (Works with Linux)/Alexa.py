import speech_recognition as sr # Library for converting speech to text.
from gtts import gTTS # Google Text-to-Speech for converting text to speech(Online Text-to-speech engine).
import pyttsx3 # Text-to-speech conversion library(Offline Text-to-speech engine).
import os # Used for operating system dependent functionality.
import datetime # To get date and time and handling them.
import webbrowser # For opening web pages.
import subprocess # For running system commands.
from playsound import playsound # For playing audio files.
import pywhatkit # For various tasks like playing YouTube videos.
from abc import ABC, abstractmethod # For creating abstract base classes.





# This is an abstract base class (ABC) that defines the interface for text-to-speech implementations. 
# It uses the ABC module and abstractmethod decorator to enforce that any subclass must implement the speak method.
class TextToSpeech(ABC):
    @abstractmethod
    def speak(self, text: str, lang: str = 'en'):
        """
        Abstract method for converting text to speech.
        
        Args:
            text (str): The text to be spoken.
            lang (str): The language in which to speak the text. Default is 'en' (English).
        """
        pass


# This class implements the TextToSpeech interface using the pyttsx3 library (offline TTS).
class Pyttsx3TTS(TextToSpeech):
    def __init__(self):
        """
        Initializes the pyttsx3 engine and sets properties such as voice, rate, and volume.
        """
        self.engine = pyttsx3.init()  # Initializes the TTS engine.
        voices = self.engine.getProperty('voices')  # Retrieves the available voices.
        self.engine.setProperty('voice', voices[2].id)  # Sets the voice to the third available voice.
        self.engine.setProperty('rate', 200)  # Sets the speech rate.
        self.engine.setProperty('volume', 1.0)  # Sets the volume to maximum.

    def speak(self, text: str, lang: str = 'en'):
        """
        Converts text to speech using pyttsx3.
        
        Args:
            text (str): The text to be spoken.
            lang (str): The language in which to speak the text. Default is 'en' (English).
        """
        self.engine.say(text)  # Adds the text to the speech queue.
        self.engine.runAndWait()  # Processes the speech queue and waits until all the text has been spoken.


# This class implements the TextToSpeech interface using the gTTS (Google Text-to-Speech) library (online TTS).
class GttsTTS(TextToSpeech):
    def speak(self, text: str, lang: str = 'en'):
        """
        Converts text to speech using gTTS.
        
        Args:
            text (str): The text to be spoken.
            lang (str): The language in which to speak the text. Default is 'en' (English).
        """
        tts = gTTS(text=text, lang=lang, slow=False)  # Creates a gTTS object with the given text and language.
        audio = "output.mp3"  # Specifies the filename to save the generated speech.
        tts.save(audio)  # Saves the speech to an MP3 file.
        playsound(audio)  # Plays the saved audio file.
        os.remove(audio)  # Deletes the audio file after playing.







# The SpeechRecognizer class is responsible for capturing and processing spoken commands using the speech_recognition library.
class SpeechRecognizer:
    def __init__(self):
        """
        Initializes the SpeechRecognizer with an instance of sr.Recognizer.
        """
        self.recognizer = sr.Recognizer()  # Provides various methods to recognize speech from an audio source.

    def catch_command(self):
        """
        Listens to the microphone for a spoken command, processes it to convert speech to text, and handles errors.
        
        Returns:
            str: The recognized command as a string, or "UNKNOWN_COMMAND" if an error occurs.
        """
        command = ""  # Initializes an empty string to store the recognized command.
        try:
            with sr.Microphone() as source:  # Opens the microphone and listens for input.
                print("Listening...")
                self.recognizer.adjust_for_ambient_noise(source)  # Adjusts for ambient noise.
                voice = self.recognizer.listen(source)  # Captures the audio data.
                command = self.recognizer.recognize_google(voice).lower()  # Converts audio to text.
                if "alexa" in command:
                    command = command.replace('alexa', '').strip()  # Removes "alexa" from the command.
                print(f"Recognized command: {command}")
        except sr.UnknownValueError:
            print("Recognized command: UNKNOWN_COMMAND")
            return "UNKNOWN_COMMAND"
        except sr.RequestError as e:
            print(f"Speech recognition request failed: {e}")
        return command  # Returns the recognized command.







# The CommandExecutor class is responsible for interpreting and executing various voice commands using a text-to-speech (TTS) engine.
class CommandExecutor:
    def __init__(self, tts: TextToSpeech):
        """
        Initializes the CommandExecutor with a given TTS engine.
        
        Args:
            tts (TextToSpeech): An instance of a text-to-speech engine.
        """
        self.tts = tts

    def execute(self, command: str):
        """
        Interprets and executes the given voice command.
        
        Args:
            command (str): The voice command to be executed.
        """
        if command == "UNKNOWN_COMMAND":
            self.tts.speak("Sorry, I didn't catch that.")
            return

        if "play" in command:
            self._play_song(command)
        elif "time" in command:
            self._tell_time()
        elif "date" in command:
            self._tell_date()
        elif "search about" in command:
            self._search_web(command)
        elif "open calculator" in command:
            self._open_calculator()
        elif "open calendar" in command:
            self._open_calendar()
        elif "exit" in command:
            self._exit()
        elif "shut down" in command:
            self._shutdown()
        else:
            self.tts.speak("Unknown command for me")
            self.tts.speak("I'm not sure how to handle that command.")

    def _play_song(self, command):
        """
        Plays a song based on the given command.
        
        Args:
            command (str): The voice command containing the song name.
        """
        song = command.replace('play', '').strip()  # Extracts the song name.
        self.tts.speak(f"Playing {song}")  # Announces the song to be played.
        pywhatkit.playonyt(song)  # Plays the song on YouTube.

    def _tell_time(self):
        """
        Announces the current time.
        """
        current_time = datetime.datetime.now().strftime('%I:%M %p')  # Gets the current time.
        self.tts.speak(f"Current time is {current_time}")  # Announces the current time.

    def _tell_date(self):
        """
        Announces the current date.
        """
        today_date = datetime.datetime.now().date().strftime("%Y-%m-%d")  # Gets the current date.
        self.tts.speak(f"Today's date is {today_date}")  # Announces the current date.

    def _search_web(self, command):
        """
        Searches the web for the given query.
        
        Args:
            command (str): The voice command containing the search query.
        """
        query = command.replace("search about", "").strip()  # Extracts the search query.
        url = f"https://www.google.com/search?q={query}"  # Constructs the search URL.
        webbrowser.open(url)  # Opens the search URL in the default web browser.
        self.tts.speak("Finished searching")  # Announces that the search is finished.

    def _open_calculator(self):
        """
        Opens the calculator application.
        """
        subprocess.run("gnome-calculator", shell=True)  # Opens the calculator application.
        self.tts.speak("Closing calculator")  # Announces that the calculator is closed.

    def _open_calendar(self):
        """
        Opens the calendar application.
        """
        subprocess.run("gnome-calendar", shell=True)  # Opens the calendar application.
        self.tts.speak("Closing calendar")  # Announces that the calendar is closed.

    def _exit(self):
        """
        Exits the application.
        """
        self.tts.speak("I will exit now")  # Announces that the application will exit.
        self.tts.speak("Goodbye Ali")  # Says goodbye to the user.
        exit()  # Exits the application.

    def _shutdown(self):
        """
        Shuts down the system.
        """
        shutdown_command = "sudo /sbin/poweroff"  # Defines the shutdown command.
        result = subprocess.run(shutdown_command, shell=True)  # Executes the shutdown command.
        if result.returncode == 0:
            self.tts.speak("System is powering off...")  # Announces that the system is shutting down.
        else:
            self.tts.speak(f"Error occurred while trying to power off. Error code: {result.returncode}")  # Announces an error with the shutdown command.






class Alexa:
    def __init__(self, tts: TextToSpeech, recognizer: SpeechRecognizer, executor: CommandExecutor):
        """
        Initializes the Alexa assistant with TTS, speech recognition, and command execution capabilities.

        Args:
            tts (TextToSpeech): An instance of a text-to-speech engine.
            recognizer (SpeechRecognizer): An instance of a speech recognizer.
            executor (CommandExecutor): An instance of a command executor.
        """
        self.tts = tts  # Text-to-speech engine instance
        self.recognizer = recognizer  # Speech recognizer instance
        self.executor = executor  # Command executor instance

    def greet(self):
        """
        Greets the user with a series of welcome messages.
        """
        self.tts.speak("Hi Ali")  # Speak "Hi Ali"
        self.tts.speak("I am Alexa")  # Speak "I am Alexa"
        self.tts.speak("I hope I can help you today")  # Speak "I hope I can help you today"

    def run(self):
        """
        Continuously listens for voice commands and executes them.
        """
        while True:
            command = self.recognizer.catch_command()  # Listen for and recognize a command
            self.executor.execute(command)  # Execute the recognized command





def main():
    """
    Main function to initialize and run the Alexa assistant.
    """
    # Flag to choose the TTS engine: set to True to use pyttsx3, False to use gTTS
    use_pyttsx3 = False

    # Initialize the TTS engine based on the flag
    tts = Pyttsx3TTS() if use_pyttsx3 else GttsTTS()

    # Initialize the speech recognizer
    recognizer = SpeechRecognizer()

    # Initialize the command executor with the chosen TTS engine
    executor = CommandExecutor(tts)

    # Initialize the Alexa assistant with the TTS engine, speech recognizer, and command executor
    alexa = Alexa(tts, recognizer, executor)

    # Greet the user
    alexa.greet()

    # Start the assistant to continuously listen and execute commands
    alexa.run()

if __name__ == "__main__":
    # Entry point of the script: call the main function
    main()
