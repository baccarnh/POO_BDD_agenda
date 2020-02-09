class Event():
    """Class that caracterise an event using his title, date,hour and description :"""

    def __init__(self, dico):

        self.title = None
        self.date = None
        self.hour = None
        self.description = None
        if dico:
            self.hydratation(dico)

    def hydratation(self, dico):
        for event_key, event_value in dico.items():
            if hasattr(self, event_key):
                setattr(self, event_key, event_value)

    def show_information(self):
        text = "------------------\n \
        title: {}\n \
        date: {}\n \
        hour: {}\n \
        description: {}\n"
        print(text.format(self.title, self.date, self.hour, self.description))