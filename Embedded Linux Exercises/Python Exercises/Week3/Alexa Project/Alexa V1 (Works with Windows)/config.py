# config.py

# Wikipedia language setting
WIKIPEDIA_LANG = "en"

# Translation settings
TRANSLATE_FROM = "de"  # Default source language (German)
TRANSLATE_TO = "en"    # Default destination language (English)

# Screenshot directory
SCREENSHOT_DIR = "Screenshot"

# Azan time settings
AZAN_CITY = "Giza"
AZAN_COUNTRY = "Egypt"

# Network analysis settings
NETWORK_ANALYSIS_DURATION = 10  # Duration in seconds for network analysis


# FOTA URL
FOTA_URL = "http://127.0.0.1:1880/ui/#!/0?socketid=QY74zGkuBidAtfaRAAAA" # "Put Your real Link here"

# Text-to-Speech settings
USE_PYTTSX3 = True  # Set to False to use gTTS instead

# Speech recognition settings
LANGUAGE = 'en-US'

# Alexa wake word
WAKE_WORD = "alexa"

# Image paths for GUI automation
IMAGE_PATHS = {
    "get_version": "GetVersion.png",
    "select_app1": "SelectApp1.png",
    "select_app2": "SelectApp2.png",
    "erase_memory": "EraseMemory.png",
    "jump_to_app": "JumpToApp.png",
    "jump_to_bootloader": "JumpToBootloader.png",
    "upload_code": "UploadCode.png",
    "select_ecu_master": "Select_ECU_Master.png",
    "select_ecu_slave": "Select_ECU_Slave.png"
}

# pyautogui automation settings
CLICK_OFFSET_X = 5
CLICK_OFFSET_Y = 5
MAX_ATTEMPTS = 5

# OpenWeatherMap API key
WEATHER_API_KEY = "57c6ac6b1b8ea0c01781254bb7d85cd0"  # "Put your real API here"
