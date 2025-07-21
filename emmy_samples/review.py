class Review:
    def __init__(self, user, rate):
        """
        Initializes a Review instance.

        Parameters:
        - user(str): user's name. 
        - rate(int or float): Rating given by the user
        """
        self._user = user
        self._rate = rate 