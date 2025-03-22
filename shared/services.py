from abc import ABC, abstractmethod
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from equipment import models as equipment_models
from django.contrib.sites.models import Site
from django.conf import settings
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



class HostManager:
    @staticmethod
    def get_base_url() -> str:
        domain = Site.objects.get_current().domain
        return domain
   
    

class QRCodeManager:
    @staticmethod
    def generate_qr_code(id):
        try:
            equipment = equipment_models.Equipment.objects.get(id=id)

            # Determine the expected QR data URL
            protocol = "http://" if settings.DEBUG else "https://"
            url = f"{protocol}{HostManager.get_base_url()}/equipment/{id}"
            qr_data = str(url)  # Ensure it's a string
            
        
            # Generate QR Code
            qr = qrcode.make(qr_data)

            # Save to in-memory buffer
            buffer = BytesIO()
            qr.save(buffer, format="PNG")
            file = ContentFile(buffer.getvalue())  # Content-only file
            
            # Save the generated QR code to the model
            equipment.qr.save(f"QR_{id}.png", file, save=True)
            print(f"QR Code for Equipment {id} generated successfully.")

        except equipment_models.Equipment.DoesNotExist:
            print(f"Error: Equipment with ID {id} not found.")

        except Exception as e:
            print(f"Error generating QR Code: {e}")
