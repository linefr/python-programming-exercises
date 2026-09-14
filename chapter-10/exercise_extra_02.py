# classes and dunder methods
class Name:
    def __init__(self,name):
        if name is None or not name.strip():
            raise ValueError('The name cannot be null or blank')
        self.name = name
        self.key = name.strip().lower()
    def __str__(self):
        return self.name
    def __repr__(self):
        return f'<Class {type(self).__name__} at 0x{id(self):x} Name: {self.name} key: {self.key}>'
    def __eq__(self, other):
        print("__eq__ called")
        return self.name == other.name
    def __lt__(self, other):
        print("__eq__ called")
        return self.name < other.name