import time
from plyer import notification

def sendNotification(title,message):
    notification.notify(title = title , message = message, timeout = 0)

if __name__ == "__main__":
    title = "Desktop Notifier"
    message = "This is a test message."
    sendNotification(title,message)

print("Notification sent successfully")