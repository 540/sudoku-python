from src.Notifier.Notifier import Notifier

class StdoutNotifier(Notifier):   
    def notify(self, message):
        print(message)