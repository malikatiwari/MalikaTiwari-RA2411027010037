from AccountRepository import AccountRepository


class Bank:
    def __init__(self, repository, notification_service):
        self.repository: AccountRepository = repository
        self.notification_service = notification_service

    def save_account(self, account):
        self.repository.save(account)

    def notify(self, message):
        self.notification_service.send(message)
