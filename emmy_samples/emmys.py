from emmy_samples.review import Review

class Nominees:

    nominations = []

    def __init__(self, title, category):
        """
        Initializes the nominees instance.
        
        Parameters:
        title(str): nominee's title
        category(str): nominee's category

        Also adds the instance to the nominations list.
        """
        self._title = title.upper()
        self._category = category.title()
        self._active = False
        self._rate = []
        Nominees.nominations.append(self)

    def __str__(self):
        """
        Returns a string representation of the nominee's title and category.
        """
        return f"{self._title} | {self._category}"
    
    @classmethod
    def list_nominations(cls):
        """
        prints a list of all nominees with their category, average rating and status.
        """
        print(f"{'Nominee👑'.ljust(25)} {'Category🎬'.ljust(22)}  {'Ratings⭐'.ljust(25)} {'Status🎥'}")
        for nominee in cls.nominations:
            print(f"{nominee._title.ljust(25)}  {nominee._category.ljust(25)} {str(nominee.average_rates).ljust(25)} {nominee.active}")

    @property
    def active(self):
        """
        Returns a status symbol indicating whether the nominee is available.
        """
        return "☑ available" if self._active else "☐ not available"
    
    def change_status(self):
        self._active = not self._active

    def get_review(self, user, rate):
        """
        Registers a user's review.
        
        Parameters:
        - user(str): user's name.
        - rate(int or float): Rating given by the user.
        
        Only accepts rating from 1 to 10.
        """
        if not (0 < rate <= 10):
            raise ValueError ("Rate must be between 1 and 10")
        
        rate = Review(user, rate)
        self._rate.append(rate)
        
    @property
    def average_rates(self):
        """
        Calculates and returns the average rating for the nominee. 
        Returns '-' if there are no ratings.
        """
        if not self._rate:
            return "-"
        rate_sum = sum(review._rate for review in self._rate)
        total_rates = len(self._rate)
        average = round(rate_sum / total_rates, 1)
        return average



