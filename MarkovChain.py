class MarkovChain:
    def __init__(self, order=1):
        self.order = order
        self.data = []

    def addData(self, newDataArray):
        if len(newDataArray) > self.order:
            for index in range(len(newDataArray)):
                print("test")
        else:
            print("ERROR: DATA < ORDER")


class MarkovNode:
    def __init__(self, key):
        self.key = key
        self.links = {}

    def addLink(self, linkKey):
        if linkKey in self.links:
            self.links[linkKey] += 1
        else:
            self.links[linkKey] = 1
