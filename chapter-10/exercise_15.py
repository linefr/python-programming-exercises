from collections import UserList

class SingleList(UserList):
    def __init__(self,class_elem, initlist=None):
        super().__init__(initlist)
        self.class_elem = class_elem

    def append(self, elem):
        self.check_type(elem)
        if elem not in self.data():
            super().append(elem)

    def extend(self, iterable):
        try:
            for elem in iterable:
                self.append(elem)
        except Exception as E:
            print(f'This is not a List')

    def __setitem__(self, position, elem):
        self.check_type(elem)
        if elem not in self.data:
            return super().__setitem__(position, elem)

    def check_type(self, elem):
        if not isinstance(elem, self.class_elem):
            raise TypeError("invalid type")

singlelist = SingleList(int)
singlelist.extend(120)
print(singlelist.data)
