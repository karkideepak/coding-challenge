"""
Object oriented programming
"""

class Authentication(object):
    def __init__(self, username=''):
        self.username = username
    
    def __lower(self):
        lower = any(c.islower() for c in self.username)
        return lower
    
    def __upper(self):
        upper = any(c.isupper() for c in self.username)
        return upper
    
    def __digit(self):
        digit = any(c.isdigit() for c in self.username)
        return digit
    
    def validate(self):
        lower = self.__lower()
        upper = self.__upper()
        digit = self.__digit()

        length = len(self.username)
        report = lower and upper and digit and length >= 6

        if report:
            print("Username is strong")
            return True

        elif not lower:
            print("Add atleast one lowercase!")
        elif not digit:
            print("You didin't use digit")
        else:
            pass

C = Authentication("outube1992")
print(C.validate())

    
    