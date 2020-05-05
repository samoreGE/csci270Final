from EpisodeGrouper import *
import random


class MarkovChain:
    def __init__(self, order=1):
        self.order = order
        self.nodes = dict()

    def addData(self, newDataArray):
        print("adding data from " + str(newDataArray))
        if len(newDataArray) >= self.order:
            nodeKey = tuple(self.makeStartingKey(newDataArray))
            for index in range(len(newDataArray) - self.order + 1):
                newKey = tuple(self.makeKey(newDataArray, index))
                nextWord = newDataArray[index+self.order-1]
                self.addToNode(nodeKey, nextWord)
                nodeKey = newKey
            self.addToNode(nodeKey, tuple(["DATAEND"]))
        else:
            print("ERROR: DATA < ORDER")

    def makeStartingKey(self, list):
        outKey = ["DATASTART"]
        for index in range(self.order):
            outKey.append(list[index])
        return outKey

    def makeKey(self, source, index):
        outKey = []
        if (index + self.order) < len(source):
            for loc in range(self.order):
                outKey.append(source[loc + index])
        return outKey

    def addToNode(self, nodeKey, linkKey):
        print("nodeKey:",nodeKey,", linkKey:",linkKey)
        if linkKey in self.getNode(nodeKey):
            self.getNode(nodeKey)[linkKey] += 1
        else:
            self.getNode(nodeKey)[linkKey] = 1
        # print("new total: ", self.getNode(nodeKey)[linkKey])

    def getNode(self, nodeKey):
        if nodeKey not in self.nodes:
            self.nodes[nodeKey] = dict()
        return self.nodes[nodeKey]

    def pickRandom(self, startNode):
        randVal = random.randrange(self.getSumOfNode(startNode))
        return randVal

    def getSumOfNode(self, node):
        nodeSum = -1
        for key in node.keys():
            nodeSum += node[key]
        print("nodeSum=" + str(nodeSum))
        return nodeSum

    def getValAtNodeLoc(self, node, loc):
        indexSum = 0
        for key in node.keys():
            indexSum += node[key]
            if indexSum >= loc:
                return key

    def getRandomNodeVal(self, node):
        if len(node.keys()) > 1:
            locVal = self.pickRandom(node)
            print("locVal=" + str(locVal))
        else:
            locVal = 0
        return self.getValAtNodeLoc(node, locVal)

    def getRandomStartingVal(self):
        x = 0
        while True:
            randomKey = random.choice(list(self.nodes.keys()))
            print(randomKey)
            if randomKey == "DATASTART":
                return randomKey

    def generate(self):
        print("Generating...")
        generatedText = ""
        currentNodeKey = tuple(["DATASTART"])
        length = 0
        while currentNodeKey[-1] != "DATAEND" and (length < 50):
            print("currentNodeKey: " + str(currentNodeKey) + ", data: " + str(self.nodes[currentNodeKey]))
            newKey = self.getRandomNodeVal(self.nodes[currentNodeKey])
            generatedText += str(newKey[-1:]) + " "
            if currentNodeKey[-1] != "DATAEND":
                currentNodeKey = newKey
            length += 1
        return generatedText


random.seed("Seinfeld Babey!")

demoChain = MarkovChain(2)
demoNames = ["MaleUnbonding", "TheDoorman", "TheExGirlfriend", "TheJacket", "ThePonyRemark", "TheStockTip"]
jerryLines = getAllCharLines(demoNames, "jerry")
print("adding lines to chain!")
for line in jerryLines:
    demoChain.addData(line.getChainableSource())
print(demoChain.generate())
