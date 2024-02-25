"""
Object oriented programming
"""

class Authentication(object):
    def __init__(self, username=''):
        self.username = username
    
    def lower(self):
        lower = any(c.islower() for c in self.username)
        return lower
    
    def upper(self):
        upper = any(c.isUpper() for c in self.username)
        return upper
    
    def digit(self):
        digit = any(c.isdigit() for c in self.username)
        return digit
    
    def validate(self):
        lower = self.lower()
        upper = self.upper()
        digit = self.digit()

        length = len(self.username)
        report = lower and upper and digit and length >= 6

    if report:
        print("Username is strong")
        retrun True
        
    elif not lower:
        print("Add atleast one lowercase!")
    elif not digit:
        print("You didin't use digit")

    
    