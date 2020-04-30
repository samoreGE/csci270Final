from EpisodeGrouper import *


class MarkovChain:
    def __init__(self, order=1):
        self.order = order
        self.nodes = dict()

    def addData(self, newDataArray):
        print("adding data from " + str(newDataArray))
        if len(newDataArray) > self.order:
            for index in range(len(newDataArray) - self.order + 1):
                print("index=", index)
                self.addToNode(self.makeKey(newDataArray, index))

        else:
            print("ERROR: DATA < ORDER")

    def makeKey(self, source, index):
        print("Making key from " + str(source))
        outKey = ""
        for loc in range(self.order):
            outKey += source[loc + index] + " "
        return outKey

    def addToNode(self, nodeKey):
        print("adding to nodeKey " + nodeKey)
        if nodeKey in self.nodes:
            self.nodes[nodeKey] += 1
        else:
            self.nodes[nodeKey] = 1
        print("new total: ")




demoChain = MarkovChain(2)
demoNames = ["MaleUnbonding", "TheDoorman", "TheExGirlfriend", "TheJacket", "ThePonyRemark", "TheStockTip"]
jerryLines = getAllCharLines(demoNames, "jerry")
for line in jerryLines:
    demoChain.addData(line.getChainableSource())
