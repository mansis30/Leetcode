class FrontMiddleBackQueue(object):

    def __init__(self):
        self.A = []

    def pushFront(self, val):
        self.A.insert(0, val)

    def pushMiddle(self, val):
        self.A.insert(len(self.A) / 2, val)

    def pushBack(self, val):
        self.A.append(val)

    def popFront(self):
        return (self.A or [-1]).pop(0)

    def popMiddle(self):
        return (self.A or [-1]).pop((len(self.A) - 1) / 2)

    def popBack(self):
        return (self.A or [-1]).pop()