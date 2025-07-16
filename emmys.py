class Nominees:
    nominations = []

    def __init__(self, title, category):
        self.title = title 
        self.category = category
        self.active = False
        Nominees.nominations.append(self)

    def __string__(self):
        return f"{self.title} | {self.category}"
    
    def list_nominations():
        for nominees in Nominees.nominations:
            print(f"{nominees.title} | {nominees.category} | {nominees.active}")

nominees_andor = Nominees("Andor", "Drama")
nominees_severance = Nominees ("Severance", "Drama")

Nominees.list_nominations()