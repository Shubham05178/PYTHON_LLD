from abc import ABC, abstractmethod
class NotificationChannel(ABC):
    @abstractmethod
    def send(self, message):
        pass
class EmailNotification(NotificationChannel):
    def send(self, message):
        print(f"Sending email notification: {message}")
class SMSNotification(NotificationChannel):
    def send(self, message):
        print(f"Sending SMS notification: {message}")
class WhatsappNotification(NotificationChannel):
    def send(self, message):
        print(f"Sending WhatsApp notification: {message}") 
class NotificationService:
    def __init__(self, channel: NotificationChannel):
        self.channel = channel
    def send_notification(self, message):
        self.channel.send(message)
notification_service = NotificationService(EmailNotification())
notification_service.send_notification("Hello, this is a test notification.")  
notification_service = NotificationService(SMSNotification())
notification_service.send_notification("Hello, this is a test notification.")  
notification_service = NotificationService(WhatsappNotification())
notification_service.send_notification("Hello, this is a test notification.")    