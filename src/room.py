# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items = None):
        self.name = name
        self.description = description
        self.items = items if items is not None else []
    def __str__(self):
        return f"{self.name} {self.description} {self.items}"
    def add_item(self, item):
        self.items.append(item)
  