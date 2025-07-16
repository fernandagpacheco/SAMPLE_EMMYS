class Nominees:
    nominations = []

    def __init__(self, title, category):
        self._title = title.upper()
        self._category = category.title()
        self._active = False
        Nominees.nominations.append(self)

    def __string__(self):
        return f"{self._title} | {self._category}"
    
    @classmethod
    def list_nominations(cls):
        print(f"{"Nominee".ljust(25)} {"Category".ljust(25)} {"Status"}")
        for nominee in cls.nominations:
            print(f"{nominee._title.ljust(25)}  {nominee._category.ljust(25)}  {nominee.active}")

    @property
    def active(self):
        return "☑" if self._active else "☐"
    
    def change_status(self):
        self._active = not self._active

nominee_andor = Nominees("Andor", "Drama")
nominee_andor.change_status()
nominee_severance = Nominees ("Severance", "Drama")

Nominees.list_nominations()