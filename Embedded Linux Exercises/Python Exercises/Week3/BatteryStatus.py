import psutil
import notify2
import time

# Initialize the notification service
notify2.init("Battery Status")

# Function to get battery status
def get_battery_status():
    battery = psutil.sensors_battery()
    percent = battery.percent
    plugged = battery.power_plugged
    return percent, plugged

# Function to send notification
def send_notification(percent, plugged):
    if plugged:
        status = "Charging"
    else:
        status = "Not Charging"
    
    message = f"Battery Status: {percent}% - {status}"
    
    notification = notify2.Notification("Battery Status", message)
    notification.show()

# Main loop to check battery status and send notification
while True:
    percent, plugged = get_battery_status()
    send_notification(percent, plugged)
    time.sleep(3)  # Check battery status every 60 seconds
