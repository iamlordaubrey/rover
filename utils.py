class CircularList(object):
    def __init__(self, iterable):
        if not iterable:
            raise ValueError
        self.iterable = iterable
        self.max_index = len(iterable) - 1

    def next(self, element):
        index = self.iterable.index(element)
        if index == self.max_index:
            index = 0
        else:
            index += 1
        return self.iterable[index]

    def previous(self, element):
        index = self.iterable.index(element)
        if index == 0:
            index = self.max_index
        else:
            index -= 1
        return self.iterable[index]


def move(cardinal_point):
    pass

