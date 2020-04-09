# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, location, items = None):
        self.name = name
        self.items = items
        self.location = location
        if self.items is None:
            self.items = []