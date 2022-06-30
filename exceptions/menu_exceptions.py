
#Exception of an inexistent menu option selected
class InexistentMenuOptionError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message

