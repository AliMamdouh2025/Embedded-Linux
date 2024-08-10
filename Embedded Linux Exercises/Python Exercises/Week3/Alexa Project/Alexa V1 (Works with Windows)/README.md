# Alexa Automation Project

## Overview

This project is designed to integrate and automate various tasks using voice commands through a custom Alexa-like voice assistant. The project includes functionality for Sending commands for FOTA by voice commands, network analysis, GUI automation, text-to-speech (TTS), speech recognition, Wikipedia integration, translation, and more. It is built to be modular, customizable, and scalable to suit a wide range of automation needs.

## Features

- **Integration With FOTA**: Alexa is integrated with FOTA by using voice commands to trigger firmware over-the-air updates through a specified URL.
- **Voice-Activated Commands**: Control diffrent systems using voice commands to execute various automated tasks(like parsing files, openning diffrent applications, search about any topic...etc.).
- **Wikipedia Integration**: Retrieve information from Wikipedia based on voice queries.
- **Azan Time Notification**: Receive notifications for prayer times based on a specified city and country.
- **Network Analysis**: Perform network traffic analysis for a defined duration.
- **Text-to-Speech**: Convert text to speech using either `pyttsx3` or `gTTS` based on user preference.
- **Speech Recognition**: Recognize and process voice commands in English (en-US).
- **GUI Automation**: Automate GUI tasks with image recognition and interaction using `pyautogui`.
- **Weather Updates**: Fetch and report weather conditions using the OpenWeatherMap API.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7 or higher
- Required Python libraries (listed in `requirements.txt`)
- Internet connection for API-based features

### Installation

 1. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Configuration:**

   Edit the `config.py` file to customize the project settings:
   
   - Enter your FOTA URL and OpenWeatherMap API key.
   - Set your desired Wikipedia language.
   - Set your city and country for Azan times.
   - Specify the duration for network analysis.
   - Choose between `pyttsx3` and `gTTS` for text-to-speech.
   - Set the language for speech recognition.

3. **Run the Project:**

   Start the main script to activate the Alexa automation:

   ```bash
   python main.py
   ```

## Configuration

The project configuration is managed through the `config.py` file. Below is a breakdown of key configuration options:

- **FOTA_URL**: URL for Firmware Over-The-Air (FOTA) updates.
- **WIKIPEDIA_LANG**: Default language for Wikipedia queries.
- **SCREENSHOT_DIR**: Directory to store screenshots taken during automation.
- **AZAN_CITY** and **AZAN_COUNTRY**: Location settings for prayer time notifications.
- **NETWORK_ANALYSIS_DURATION**: Time in seconds for conducting network analysis.
- **USE_PYTTSX3**: Toggle between `pyttsx3` (True) and `gTTS` (False) for TTS.
- **LANGUAGE**: Language code for speech recognition (e.g., 'en-US').
- **WEATHER_API_KEY**: API key for accessing weather data.

## Usage

- **Voice Commands**: Simply say voice command defined in command executer class. The assistant will process and execute the task.
- **Wikipedia Search**: Request information by stating the topic you want to know about.
- **Azan Time**: The system will notify you of prayer times based on your location.
- **Network Analysis**: The assistant will monitor network traffic for the specified duration.
- **Weather Information**: Get real-time weather updates by asking for the weather.

## Troubleshooting

- **Voice Recognition Issues**: Ensure your microphone is working properly and that the language setting matches your spoken language.
- **API Key Errors**: Double-check that your API keys (e.g., OpenWeatherMap) are correctly entered in `config.py`.
- **GUI Automation Failures**: Ensure the images in `IMAGE_PATHS` match the actual elements on your screen.

## For more clarification about our FOTA project go to this link
https://github.com/ShehabAldeenMo/Fireware-Over-The-Air
