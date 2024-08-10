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
import scapy.all as scapy
from scapy.layers import http
import pandas as pd
from openpyxl import Workbook
import tkinter as tk
from tkinter import messagebox
from Files import read_file, write_to_file, delete_file, create_file, parse_c_functions, save_to_excel
import wikipedia
from googletrans import Translator
import psutil
from PIL import ImageGrab
import datetime








class TextToSpeech(ABC):
    """
    Abstract base class for text-to-speech implementations.
    This class defines the interface for converting text to speech,
    allowing for different concrete implementations.
    """
    @abstractmethod
    def speak(self, text: str, lang: str = 'en'):
        """
        Convert text to speech.
        This abstract method should be implemented by subclasses to
        provide specific text-to-speech functionality.
        """

        pass


class Pyttsx3TTS(TextToSpeech):
    """
    Offline text-to-speech implementation using pyttsx3.
    This class provides a local, offline solution for text-to-speech
    conversion, which can be faster and more reliable in situations
    without internet connectivity.
    """
    def __init__(self):
        """
        Initialize the pyttsx3 engine with specific voice and speech settings.
        """
        self.engine = pyttsx3.init()  # Initialize pyttsx3 engine
        voices = self.engine.getProperty('voices')  # Get available voices
        self.engine.setProperty('voice', voices[2].id)  # Set voice (index 2)
        self.engine.setProperty('rate', 200)  # Set speech rate
        self.engine.setProperty('volume', 1.0)  # Set volume to maximum

    def speak(self, text: str, lang: str = 'en'):
        """
        Convert text to speech using pyttsx3.
        This method queues the given text and immediately speaks it
        using the configured pyttsx3 engine.
        """
        self.engine.say(text)  # Queue the text to be spoken
        self.engine.runAndWait()  # Speak the queued text


class GttsTTS(TextToSpeech):
    """
    Online text-to-speech implementation using Google Text-to-Speech.
    This class provides an internet-dependent solution for text-to-speech
    conversion, which can offer a wider range of voices and languages.
    """
    def speak(self, text: str, lang: str = 'en'):
        """
        Convert text to speech using gTTS and play it.
        This method creates an audio file, saves it temporarily,
        plays it using pygame, and then removes the file.
        """
        tts = gTTS(text=text, lang=lang, slow=False)  # Create gTTS object
        audio = "output.mp3"  # Temporary audio file name
        tts.save(audio)  # Save speech to audio file
        pygame.mixer.music.load(audio)  # Load audio file
        pygame.mixer.music.play()  # Play audio
        while pygame.mixer.music.get_busy():  # Wait for audio to finish
            pygame.time.Clock().tick(10)
        os.remove(audio)  # Remove temporary audio file








class SpeechRecognizer:
    """
    Class for recognizing speech input.
    This class utilizes the speech_recognition library to capture
    and interpret voice commands from the user.
    """
    def __init__(self):
        """
        Initialize the speech recognizer.
        """
        self.recognizer = sr.Recognizer()  # Initialize speech recognizer

    def catch_command(self):
        """
        Listen for a voice command and return the recognized text.
        This method adjusts for ambient noise, listens for voice input,
        and uses Google Speech Recognition to interpret the command.
        It also handles potential errors during the recognition process.
        """
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
    This function uses pyautogui to find a specific image on the screen,
    move the cursor to its location (with optional offset), and optionally click it.
    It attempts to find the image multiple times before giving up.
    
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
        location = pyautogui.locateOnScreen(image)  # Try to locate the image on screen
        if location is not None:
            pyautogui.moveTo(location[0] + x_shift, location[1] + y_shift, duration=0.5)  # Move to image location with offset
            if is_clicked:
                pyautogui.click()  # Click if required
            return True
        time.sleep(2)  # Wait before next attempt
    print(f"Image '{image}' not found on the screen after {max_attempts} attempts.")
    return False








# Weather Functions
def get_weather(city):
    """
    Retrieve weather information for a specified city.
    This function uses the OpenWeatherMap API to fetch current weather data
    for the given city, including temperature, pressure, humidity, and description.
    
    Args:
    city (str): Name of the city for which to retrieve weather information
    
    Returns:
    dict: Weather data including min/max temperature, pressure, humidity, and description,
          or None if the request fails
    """
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








def capture_traffic(duration):
    """
    Capture network traffic for a specified duration.
    This function uses scapy to sniff network packets for the given time period.
    
    Args:
    duration (int): Duration in seconds for which to capture traffic
    
    Returns:
    list: Captured network packets
    """
    packets = scapy.sniff(timeout=duration)
    return packets


def analyze_packets(packets):
    """
    Analyze captured network packets.
    This function processes the captured packets, extracting relevant information
    such as timestamp, source/destination IP, protocol, and packet details.
    It handles various protocols including TCP, UDP, ICMP, ARP, and HTTP.
    
    Args:
    packets (list): List of captured network packets
    
    Returns:
    list: Analyzed packet data in a structured format
    """
    
    # Initialize an empty list to store the analyzed packet data.
    data = []

    # Set the start_time to the timestamp of the first packet, or 0 if the packets list is empty.
    start_time = packets[0].time if packets else 0

    # Iterate over each packet in the packets list, with the index starting from 1.
    for i, pkt in enumerate(packets, start=1):
        
        # Calculate the relative timestamp of the packet by subtracting the start_time.
        timestamp = f"{pkt.time - start_time:.6f}"

        # Extract the source IP address if the packet contains an IP layer; otherwise, use the default src attribute.
        src_ip = pkt[scapy.IP].src if scapy.IP in pkt else pkt.src

        # Extract the destination IP address if the packet contains an IP layer; otherwise, use the default dst attribute.
        dst_ip = pkt[scapy.IP].dst if scapy.IP in pkt else pkt.dst

        # Initialize the protocol as "Unknown" for packets that do not match known protocols.
        protocol = "Unknown"

        # Determine the length of the packet.
        length = len(pkt)

        # Initialize an empty string to store additional packet information.
        info = ""

        # Check if the packet contains a TCP layer.
        if scapy.TCP in pkt:
            protocol = "TCP"  # Set the protocol to TCP.

            # Extract source and destination ports, TCP flags, sequence number, acknowledgment number, and window size.
            sport, dport = pkt[scapy.TCP].sport, pkt[scapy.TCP].dport
            flags = pkt[scapy.TCP].flags
            seq, ack = pkt[scapy.TCP].seq, pkt[scapy.TCP].ack
            win = pkt[scapy.TCP].window

            # Construct the info string with TCP-specific details.
            info = f"{sport} → {dport} [{flags}] Seq={seq} Ack={ack} Win={win} Len={length}"

            # Check if the ports match known MQTT ports (1883 or 8883).
            if sport == 1883 or dport == 1883 or sport == 8883 or dport == 8883:
                protocol = "MQTT"  # Set the protocol to MQTT.

                # Check if the TCP payload is not empty.
                if bytes(pkt[scapy.TCP].payload):
                    mqtt_type = bytes(pkt[scapy.TCP].payload)[0] >> 4  # Extract MQTT message type.

                    # Dictionary mapping MQTT types to their names.
                    mqtt_types = {1: "CONNECT", 3: "PUBLISH", 4: "PUBACK", 8: "SUBSCRIBE", 13: "PINGREQ"}

                    # Append MQTT-specific information to the info string.
                    info = f"{mqtt_types.get(mqtt_type, 'Unknown')} {info}"

        # Check if the packet contains a UDP layer.
        elif scapy.UDP in pkt:
            protocol = "UDP"  # Set the protocol to UDP.

            # Extract source and destination ports.
            sport, dport = pkt[scapy.UDP].sport, pkt[scapy.UDP].dport

            # Construct the info string with UDP-specific details.
            info = f"{sport} → {dport} Len={length}"

            # Check if the ports match the DNS port (53).
            if sport == 53 or dport == 53:
                protocol = "DNS"  # Set the protocol to DNS.

                # Check if the packet contains a DNS layer.
                if scapy.DNS in pkt:
                    # Determine if the packet is a DNS query or response.
                    qr = "Response" if pkt[scapy.DNS].qr else "Query"

                    # Extract the queried domain name.
                    if pkt[scapy.DNS].qd:
                        qname = pkt[scapy.DNS].qd.qname.decode()

                        # Append DNS-specific information to the info string.
                        info = f"{qr} {qname}"

        # Check if the packet contains an ICMP layer.
        elif scapy.ICMP in pkt:
            protocol = "ICMP"  # Set the protocol to ICMP.

            # Extract the ICMP type and code.
            icmp_type = pkt[scapy.ICMP].type
            icmp_code = pkt[scapy.ICMP].code

            # Construct the info string with ICMP-specific details.
            info = f"Type={icmp_type} Code={icmp_code}"

        # Check if the packet contains an ARP layer.
        elif scapy.ARP in pkt:
            protocol = "ARP"  # Set the protocol to ARP.

            # Determine if the ARP packet is a request or reply.
            op = "Request" if pkt[scapy.ARP].op == 1 else "Reply"

            # Extract source and destination MAC addresses.
            src_mac = pkt[scapy.ARP].hwsrc
            dst_mac = pkt[scapy.ARP].hwdst

            # Construct the info string with ARP-specific details.
            info = f"{op} {src_mac} → {dst_mac}"

        # Check if the packet contains an HTTP layer.
        elif http.HTTP in pkt:
            protocol = "HTTP"  # Set the protocol to HTTP.

            # Check if the packet is an HTTP request and extract the method and path.
            if pkt[http.HTTP].Method:
                info = f"{pkt[http.HTTP].Method} {pkt[http.HTTP].Path}"

            # Check if the packet is an HTTP response and extract the status code.
            elif pkt[http.HTTP].Status_Code:
                info = f"Status: {pkt[http.HTTP].Status_Code}"

        # Append the analyzed packet data as a list to the data list.
        data.append([i, timestamp, src_ip, dst_ip, protocol, length, info])

    # Return the list containing the analyzed packet data.
    return data


def save_network_analyze_to_excel(data, filename):
    """
    Save analyzed network data to an Excel file.
    This function takes the structured network analysis data and saves it
    to an Excel file for easy viewing and further analysis.
    
    Args:
    data (list): Analyzed network data
    filename (str): Name of the Excel file to save
    """
    df = pd.DataFrame(data, columns=["No.", "Time", "Source", "Destination", "Protocol", "Length", "Info"])
    df.to_excel(filename, index=False, engine='openpyxl')








def get_prayer_times(city, country, method=5):
    """
    Retrieve prayer times for a specified city and country.
    This function uses the Aladhan API to fetch prayer times based on
    the given location and calculation method.
    
    Args:
    city (str): Name of the city
    country (str): Name of the country
    method (int): Calculation method for prayer times
    
    Returns:
    dict: Prayer times for various prayers, or None if the request fails
    """
    url = f'http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method={method}'
    response = requests.get(url)
    data = response.json()

    if data['code'] == 200:
        return data['data']['timings']
    else:
        return None


def display_prayer_times(prayer_times):
    """
    Display prayer times in a graphical user interface.
    This function creates a Tkinter window to show the prayer times
    in a user-friendly format.
    
    Args:
    prayer_times (dict): Dictionary containing prayer times
    """
    root = tk.Tk()
    root.title("Prayer Times")

    tk.Label(root, text="Prayer Times", font=('Helvetica', 16, 'bold')).pack(pady=10)

    for prayer, time in prayer_times.items():
        tk.Label(root, text=f"{prayer}: {time}", font=('Helvetica', 14)).pack(pady=5)

    root.mainloop()







class CommandExecutor:
    """
    Class for executing various voice commands.
    This class handles the interpretation and execution of different
    voice commands, including file operations, web searches, system commands,
    and custom actions like weather retrieval and FOTA operations.
    """
    def __init__(self, tts: TextToSpeech):
        """
        Initialize the CommandExecutor with a text-to-speech engine.
        """
        self.tts = tts  # Text-to-speech engine

    def execute(self, command: str):
        """
        Execute the given voice command.
        This method interprets the voice command and calls the appropriate
        method to handle the requested action.
        """
        if command == "UNKNOWN_COMMAND":
            self.tts.speak("Sorry, I didn't catch that.")
            return

        # Check for various commands and call appropriate methods
        if "get weather of" in command:
            self._get_weather(command)
        elif "read file" in command:
            self._read_file()
        elif "write file" in command:
            self._write_file()
        elif "delete file" in command:
            self._delete_file()
        elif "create file" in command:
            self._create_file()
        elif "parsing file" in command:
            self._parse_file()
        elif "prayer" in command:
            self._get_azan_times()   
        elif "network" in command:
            self._analyze_network()                      
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
        elif "translate" in command:
            text_to_translate = command.replace("translate", "").strip()
            translated_text = self._translate_text(text_to_translate)
            self.tts.speak(f"The translation is: {translated_text}")
        elif "speak about" in command:
            topic = command.replace("speak about", "").strip()
            info = self._get_wikipedia_paragraph(topic)
            self.tts.speak(info)
        elif "take screenshot" in command:
            screenshot_file = self._take_screenshot()
            self.tts.speak(f"Screenshot saved as {screenshot_file}")
        elif "battery" in command:
            battery_status = self._get_battery_status()
            self.tts.speak(battery_status)            
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

    def _analyze_network(self):
        self.tts.speak("Starting network analysis. This may take a few moments.")
        duration = config.NETWORK_ANALYSIS_DURATION
        print(f"Capturing network traffic for {duration} seconds...")
        packets = capture_traffic(duration)

        print("Analyzing packets...")
        data = analyze_packets(packets)

        filename = "network_analysis.xlsx"
        print(f"Saving analysis to {filename}...")
        save_network_analyze_to_excel(data, filename)

        self.tts.speak(f"Network analysis complete. Results saved to {filename}")
        print("Analysis complete!")
    def _read_file(self):
        self.tts.speak("Please enter the name of the file you want to read.")
        file_name = input("Enter file name: ")
        content = read_file(file_name)
        if content:
            self.tts.speak(f"Content of {file_name}:")
            self.tts.speak(content)
        else:
            self.tts.speak(f"Unable to read {file_name}")

    def _write_file(self):
        self.tts.speak("Please enter the name of the file you want to write to.")
        file_name = input("Enter file name: ")
        self.tts.speak("Please enter the content you want to write.")
        content = input("Enter content: ")
        write_to_file(file_name, content)
        self.tts.speak(f"Content has been written to {file_name}")

    def _delete_file(self):
        self.tts.speak("Please enter the name of the file you want to delete.")
        file_name = input("Enter file name: ")
        delete_file(file_name)
        self.tts.speak(f"{file_name} has been deleted")

    def _create_file(self):
        self.tts.speak("Please enter the name of the file you want to create.")
        file_name = input("Enter file name: ")
        created_file = create_file(file_name)
        if created_file:
            self.tts.speak(f"{file_name} has been created")
        else:
            self.tts.speak(f"Unable to create {file_name}")

    def _parse_file(self):
        self.tts.speak("Please enter the name of the file you want to parse.")
        file_name = input("Enter file name: ")
        functions = parse_c_functions(file_name)
        if functions:
            output_file = f"{os.path.splitext(file_name)[0]}_Parsed.xlsx"
            save_to_excel(functions, output_file)
            self.tts.speak(f"Parsing complete. Results saved to {output_file}")
        else:
            self.tts.speak(f"Unable to parse {file_name}")

    def _translate_text(self, text):
        translator = Translator()
        translation = translator.translate(text, src=config.TRANSLATE_FROM, dest=config.TRANSLATE_TO)
        return translation.text

    def _get_wikipedia_paragraph(self, topic):
        wikipedia.set_lang(config.WIKIPEDIA_LANG)
        try:
            summary = wikipedia.summary(topic, sentences=2)
            return summary
        except wikipedia.exceptions.DisambiguationError as e:
            return f"Disambiguation error: {e.options}. Please be more specific."
        except wikipedia.exceptions.PageError:
            return "Sorry, the topic does not exist on Wikipedia."

    def _get_battery_status(self):
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percent = battery.percent
        status = f"Battery is {'plugged in' if plugged else 'not plugged in'}. "
        status += f"Battery percentage: {percent}%"
        return status

    def _take_screenshot(self):
        if not os.path.exists(config.SCREENSHOT_DIR):
            os.makedirs(config.SCREENSHOT_DIR)
        screenshot = ImageGrab.grab()
        filename = f"screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        filepath = os.path.join(config.SCREENSHOT_DIR, filename)
        screenshot.save(filepath)
        return filepath

    def _tell_time(self):
        """Tell the current time."""
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        self.tts.speak(f"Current time is {current_time}")

    def _get_azan_times(self):
        self.tts.speak(f"Getting prayer times for {config.AZAN_CITY}, {config.AZAN_COUNTRY}")
        prayer_times = get_prayer_times(config.AZAN_CITY, config.AZAN_COUNTRY)
        
        if prayer_times:
            self.tts.speak("Prayer times retrieved successfully. Displaying them now.")
            display_prayer_times(prayer_times)
        else:
            self.tts.speak("Sorry, I couldn't retrieve the prayer times.")        

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
    """
    Main class for the Alexa-like assistant.
    This class integrates speech recognition, text-to-speech, and command execution
    to create a voice-controlled assistant that can perform various tasks.
    """
    def __init__(self, tts: TextToSpeech, recognizer: SpeechRecognizer, executor: CommandExecutor):
        """
        Initialize the Alexa assistant with necessary components.
        """
        self.tts = tts
        self.recognizer = recognizer
        self.executor = executor

    def greet(self):
        """
        Greet the user with a welcome message.
        This method is called when the assistant starts up.
        """
        self.tts.speak("Hi Ali")
        self.tts.speak("I am Alexa")
        self.tts.speak("I hope I can help you today")

    def run(self):
        """
        Main loop to continuously listen for and execute commands.
        This method keeps the assistant running, constantly listening for
        voice commands and executing them until the program is terminated.
        """
        while True:
            command = self.recognizer.catch_command()
            self.executor.execute(command)








def main():
    """
    Main function to set up and run the Alexa-like assistant.
    This function initializes all necessary components (TTS, speech recognition,
    command executor) and starts the Alexa assistant.
    """   
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