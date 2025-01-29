from abc import ABC, abstractmethod

# Abstraction
class Notification(ABC):
    @abstractmethod
    def send(self):
        pass

# High-level module, depends on abstraction
class NotificationService:
    def __init__(self, notification: Notification) -> None:
        self.notification = notification

    def send_notification(self):
        self.notification.send()

# Low-level modules, implementing the abstraction
class EmailNotificationWithSMTP(Notification):
    def __init__(self, msg) -> None:
        self.msg = msg

    def send(self):
        print(f"Sending email using SMTP: {self.msg}")

class EmailNotificationWithSendGrid(Notification):
    def __init__(self, msg) -> None:
        self.msg = msg

    def send(self):
        print(f"Sending email using SendGrid: {self.msg}")

