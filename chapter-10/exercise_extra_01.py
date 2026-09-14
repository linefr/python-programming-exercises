class SuperClass():
    def __init__(self):
        self.superclass = {10,20,30}

class SubClass(SuperClass):
    def __init__(self):
        super().__init__()
        self.subclass = self.superclass
        self.superclass = 5
        self.new_subclass = self.superclass 


subclass = SubClass()
superclass = SuperClass()
print(subclass.subclass)
print(subclass.new_subclass)
print(superclass.superclass)

print(iter(superclass.superclass))
