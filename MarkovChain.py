from EpisodeGrouper import *


class MarkovChain:
    def __init__(self, order=1):
        self.order = order
        self.nodes = dict()

    def addData(self, newDataArray):
        print("adding data from " + str(newDataArray))
        if len(newDataArray) > self.order:
            nodeKey = "DATASTART"
            for index in range(len(newDataArray) - self.order + 1):
                newKey = self.makeKey(newDataArray, index)
                self.addToNode(nodeKey, newKey)
                nodeKey = newKey
            self.addToNode(nodeKey, "DATAEND")
        else:
            print("ERROR: DATA < ORDER")

    def makeKey(self, source, index):
        outKey = ""
        for loc in range(self.order):
            outKey += source[loc + index] + " "
        return outKey

    def addToNode(self, nodeKey, linkKey):
        print("nodeKey: " + nodeKey + ", linkKey: " + linkKey)
        if linkKey in self.getNode(nodeKey):
            self.getNode(nodeKey)[linkKey] += 1
        else:
            self.getNode(nodeKey)[linkKey] = 1
        print("new total: ", self.getNode(nodeKey)[linkKey])

    def getNode(self, nodeKey):
        if nodeKey not in self.nodes:
            self.nodes[nodeKey] = dict()
        return self.nodes[nodeKey]


demoChain = MarkovChain(1)
demoNames = ["MaleUnbonding", "TheDoorman", "TheExGirlfriend", "TheJacket", "ThePonyRemark", "TheStockTip"]
jerryLines = getAllCharLines(demoNames, "jerry")
for line in jerryLines:
    demoChain.addData(line.getChainableSource())
