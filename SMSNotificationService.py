from NotificationService import NotificationService


class SMSNotificationService(NotificationService):

    def send(self, message):
        print(f"SMS: {message}")
