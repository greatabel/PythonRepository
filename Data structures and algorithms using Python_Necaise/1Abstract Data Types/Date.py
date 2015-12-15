class Date :

    def __init__(self, month, day, year):
        self._julianDay = 0
        assert self._isValidGregorian( month, day, year ), \
                "Invalid Gregorian date"
        
        