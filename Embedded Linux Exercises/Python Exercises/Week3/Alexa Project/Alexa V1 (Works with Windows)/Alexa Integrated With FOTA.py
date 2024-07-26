import speech_recognition as sr  # Library for speech recognition
from gtts import gTTS  # Google Text-to-Speech library
import pyttsx3  # Offline text-to-speech library
import os  # For file operations
import datetime  # For date and time operations
import webbrowser  # For opening web pages
import subprocess  # For running system commands
import pywhatkit  # For playing YouTube videos
from abc import ABC, abstractmethod  # For creating abstract base classes
import pygame  # For audio playback
import pyautogui  # For GUI automation
import time  # For adding delays
import requests
import config




class TextToSpeech(ABC):
    """Abstract base class for text-to-speech implementations."""
    @abstractmethod
    def speak(self, text: str, lang: str = 'en'):
        """Convert text to speech."""
        pass

class Pyttsx3TTS(TextToSpeech):
    """Offline text-to-speech implementation using pyttsx3."""
    def __init__(self):
        self.engine = pyttsx3.init()  # Initialize pyttsx3 engine
        voices = self.engine.getProperty('voices')  # Get available voices
        self.engine.setProperty('voice', voices[2].id)  # Set voice (index 2)
        self.engine.setProperty('rate', 200)  # Set speech rate
        self.engine.setProperty('volume', 1.0)  # Set volume to maximum

    def speak(self, text: str, lang: str = 'en'):
        """Convert text to speech using pyttsx3."""
        self.engine.say(text)  # Queue the text to be spoken
        self.engine.runAndWait()  # Speak the queued text

class GttsTTS(TextToSpeech):
    """Online text-to-speech implementation using Google Text-to-Speech."""
    def speak(self, text: str, lang: str = 'en'):
        """Convert text to speech using gTTS and play it."""
        tts = gTTS(text=text, lang=lang, slow=False)  # Create gTTS object
        audio = "output.mp3"  # Temporary audio file name
        tts.save(audio)  # Save speech to audio file
        pygame.mixer.music.load(audio)  # Load audio file
        pygame.mixer.music.play()  # Play audio
        while pygame.mixer.music.get_busy():  # Wait for audio to finish
            pygame.time.Clock().tick(10)
        os.remove(audio)  # Remove temporary audio file

class SpeechRecognizer:
    """Class for recognizing speech input."""
    def __init__(self):
        self.recognizer = sr.Recognizer()  # Initialize speech recognizer

    def catch_command(self):
        """Listen for a voice command and return the recognized text."""
        command = ""
        try:
            with sr.Microphone() as source:  # Use microphone as audio source
                print("Listening...")
                self.recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
                voice = self.recognizer.listen(source)  # Listen for voice input
                command = self.recognizer.recognize_google(voice).lower()  # Recognize speech using Google Speech Recognition
                if "alexa" in command:
                    command = command.replace('alexa', '').strip()  # Remove 'alexa' from command
                print(f"Recognized command: {command}")
        except sr.UnknownValueError:
            print("Recognized command: UNKNOWN_COMMAND")
            return "UNKNOWN_COMMAND"
        except sr.RequestError as e:
            print(f"Speech recognition request failed: {e}")
        return command




def locate(image, x_shift=0, y_shift=0, is_clicked=False, max_attempts=5):
    """
    Locate an image on the screen and optionally click it.
    
    Args:
    image (str): Path to the image file to locate
    x_shift (int): Horizontal pixel shift from the located image
    y_shift (int): Vertical pixel shift from the located image
    is_clicked (bool): Whether to click the located image
    max_attempts (int): Maximum number of attempts to locate the image
    
    Returns:
    bool: True if image was found, False otherwise
    """
    for attempt in range(max_attempts):
        location = pyautogui.locateOnScreen(config.IMAGE_PATHS[image])  # Try to locate the image on screen
        if location is not None:
            pyautogui.moveTo(location[0] + config.CLICK_OFFSET_X, location[1] + config.CLICK_OFFSET_Y, duration=0.5)  # Move to image location with offset
            if is_clicked:
                pyautogui.click()  # Click if required
            return True
        time.sleep(1)  # Wait before next attempt
    print(f"Image '{image}' not found on the screen after {max_attempts} attempts.")
    return False

def get_weather(city):
    api_key = config.WEATHER_API_KEY  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }




    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return {
            "min_temp": data["main"]["temp_min"],
            "max_temp": data["main"]["temp_max"],
            "pressure": data["main"]["pressure"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
        }
    else:
        return None

class CommandExecutor:
    """Class for executing various commands."""
    def __init__(self, tts: TextToSpeech):
        self.tts = tts  # Text-to-speech engine

    def execute(self, command: str):
        """Execute the given command."""
        if command == "UNKNOWN_COMMAND":
            self.tts.speak("Sorry, I didn't catch that.")
            return

        # Check for various commands and call appropriate methods
        if "get weather of" in command:
            self._get_weather(command)
        elif "get version" in command:
            self._perform_fota_action("get version")
        elif "select first application" in command:
            self._perform_fota_action("select first application")
        elif "select second application" in command:
            self._perform_fota_action("select second application")
        elif "erase memory" in command:
            self._perform_fota_action("erase memory")
        elif "jump to app" in command:
            self._perform_fota_action("jump to application")
        elif "jump to bootloader" in command:
            self._perform_fota_action("jump to bootloader")
        elif "write to memory" in command:
            self._perform_fota_action("write to memory")
        elif "select ecu master" in command:
            self._perform_fota_action("select ecu master")
        elif "select ecu slave" in command:
            self._perform_fota_action("select ecu slave")
        elif "play" in command:
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
        else:
            self.tts.speak("Unknown command for me")
            self.tts.speak("I'm not sure how to handle that command.")

    def _perform_fota_action(self, action):
        """Perform FOTA (Firmware Over The Air) related actions."""
        url = config.FOTA_URL
        webbrowser.open_new_tab(url)  # Open FOTA web interface
        time.sleep(2)  # Wait for the page to load

        pyautogui.scroll(-650)  # Scroll down

        # Perform specific action based on the command
        if action == "get version":
            pyautogui.scroll(650)  # Scroll up          
            locate("GetVersion.png", x_shift=20, y_shift=20, is_clicked=True)
        elif action == "select first application":
            locate("SelectApp1.png", x_shift=20, y_shift=20, is_clicked=True)
        elif action == "select second application":
            locate("SelectApp2.png", x_shift=20, y_shift=20, is_clicked=True)
        elif action == "erase memory":
            locate("EraseMemory.png", x_shift=20, y_shift=20, is_clicked=True)
        elif action == "jump to application":
            locate("JumpToApp.png", x_shift=20, y_shift=20, is_clicked=True)
        elif action == "jump to bootloader":
            locate("JumpToBootloader.png", x_shift=20, y_shift=20, is_clicked=True)
        elif action == "write to memory":
            locate("UploadCode.png", x_shift=20, y_shift=20, is_clicked=True)
        elif action == "select ecu master":
            locate("Select_ECU_Master.png", x_shift=20, y_shift=20, is_clicked=True)
        elif action == "select ecu slave":
            locate("Select_ECU_Slave.png", x_shift=20, y_shift=20, is_clicked=True)

        self.tts.speak(f"Performed {action} action")

    def _play_song(self, command):
        """Play a song on YouTube."""
        song = command.replace('play', '').strip()  # Extract song name from command
        self.tts.speak(f"Playing {song}")
        pywhatkit.playonyt(song)  # Play song on YouTube

    def _tell_time(self):
        """Tell the current time."""
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        self.tts.speak(f"Current time is {current_time}")

    def _tell_date(self):
        """Tell the current date."""
        today_date = datetime.datetime.now().date().strftime("%Y-%m-%d")
        self.tts.speak(f"Today's date is {today_date}")

    def _search_web(self, command):
        """Perform a web search."""
        query = command.replace("search about", "").strip()  # Extract search query
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)  # Open search results in browser
        self.tts.speak("Finished searching")

    def _open_calculator(self):
        """Open the calculator application."""
        subprocess.run("start calculator:", shell=True)
        self.tts.speak("Calculator is opened")

    def _open_calendar(self):
        """Open the calendar application."""
        subprocess.run("start outlookcal:", shell=True)
        self.tts.speak("Calendar is opened")

    def _exit(self):
        """Exit the application."""
        self.tts.speak("I will exit now")
        self.tts.speak("Goodbye Ali")
        exit()

    def _get_weather(self, command):
        city = command.replace("get weather of", "").strip()
        weather_data = get_weather(city)
        if weather_data:
            weather_message = (
                f"Weather in {city} is:\n"
                f"Min Temperature: {weather_data['min_temp']}°C\n"
                f"Max Temperature: {weather_data['max_temp']}°C\n"
                f"Pressure: {weather_data['pressure']} hPa\n"
                f"Humidity: {weather_data['humidity']}%\n"
                f"Description: {weather_data['description']}"
            )
            print(weather_message)  # Print to console
            self.tts.speak(weather_message)  # Speak the weather information
        else:
            self.tts.speak(f"Sorry, I couldn't get the weather information for {city}")    

        


class Alexa:
    """Main class for the Alexa-like assistant."""
    def __init__(self, tts: TextToSpeech, recognizer: SpeechRecognizer, executor: CommandExecutor):
        self.tts = tts
        self.recognizer = recognizer
        self.executor = executor

    def greet(self):
        """Greet the user."""
        self.tts.speak("Hi Ali")
        self.tts.speak("I am Alexa")
        self.tts.speak("I hope I can help you today")

    def run(self):
        """Main loop to continuously listen for and execute commands."""
        while True:
            command = self.recognizer.catch_command()
            self.executor.execute(command)

def main():
    """Main function to set up and run the Alexa-like assistant."""    
    pygame.mixer.init() # Initialize pygame mixer for audio playback
    use_pyttsx3 = True  # When on Windows, it is preferred to make this True. In Linux, make this False
    tts = Pyttsx3TTS() if use_pyttsx3 else GttsTTS()  # Choose TTS engine based on platform
    recognizer = SpeechRecognizer()
    executor = CommandExecutor(tts)
    alexa = Alexa(tts, recognizer, executor)
    alexa.greet()
    alexa.run()

if __name__ == "__main__":
    main()