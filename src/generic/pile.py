import random


class Pile(object):

    def __init__(self):
        self.__members = []

    @property
    def members(self):
        return self.__members

    @property
    def size(self):
        return len(self.members)

    def shuffle(self):
        random.shuffle(self.__members)

    def put(self, obj):
        self.__members.insert(0, obj)

    def put_below(self, obj):
        self.__members.append(obj)

    def get(self):
        if not self.__members:
            return None
        return self.__members.pop(0)

    def see(self, index=0):
        if not self.__members:
            return None
        size = len(self.__members)
        if index >= size:
            index = size - 1
        if index < -size:
            index = -size
        return self.__members[index]

    def clean(self):
        self.__members = []

    def empty(self):
        return not self.__members
