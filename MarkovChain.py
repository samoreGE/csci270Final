from EpisodeGrouper import *
import random


class MarkovChain:
    def __init__(self, order):
        self.order = order
        self.nodes = dict()

    def addData(self, newDataArray):
        # print("adding data from " + str(newDataArray))
        if len(newDataArray) >= self.order:
            for index in range(-1, len(newDataArray)):
                self.addDataAtIndex(newDataArray, index)
        else:
            print("ERROR: DATA < ORDER")

    def makeStartingKey(self, list):
        outKey = ["DATASTART"]
        for index in range(self.order - 1):
            outKey.append(list[index])
        return outKey

    def addDataAtIndex(self, dataArray, index):
        # print("index=" + str(index))
        if index < 0:
            nodeKey = tuple(self.makeStartingKey(dataArray))
            nextWord = dataArray[self.order - 1]
            self.addToNode(nodeKey, nextWord)
        elif index < (len(dataArray) - self.order):
            nextWord = dataArray[index + self.order]
            nodeKey = tuple(self.makeKey(dataArray, index))
            self.addToNode(nodeKey, nextWord)
        elif index == (len(dataArray) - self.order):
            nextWord = "DATAEND"
            nodeKey = tuple(self.makeKey(dataArray, index))
            self.addToNode(nodeKey, nextWord)

    def makeKey(self, source, index):
        outKey = []
        if (index + self.order) <= len(source):
            for loc in range(self.order):
                outKey.append(source[loc + index])
        return outKey

    def addToNode(self, nodeKey, linkKey):
        # print("nodeKey:", nodeKey, ", linkKey:", linkKey)
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
        else:
            locVal = 0
        return self.getValAtNodeLoc(node, locVal)

    def getRandomStartingVal(self):
        print("finding start...")
        x = 0
        while True:
            randomKey = random.choice(list(self.nodes.keys()))
            if randomKey[0] == "DATASTART":
                return randomKey

    def makeStartingText(self, startKey):
        startText = ""
        if startKey[0] == "DATASTART":
            for i in range(1, len(startKey)):
                startText += str(startKey[i]) + " "
        else:
            print("ERROR, needs a StartingText!")
        return startText

    def generate(self, limit):
        print("Generating...")
        currentNodeKey = tuple(self.getRandomStartingVal())
        generatedText = self.makeStartingText(currentNodeKey)
        length = 0
        while length < limit:
            print("currentNodeKey: " + str(currentNodeKey) + ", data: " + str(self.nodes[currentNodeKey]))
            newWord = self.getRandomNodeVal(self.nodes[currentNodeKey])
            if newWord != "DATAEND":
                generatedText += str(newWord) + " "
                currentNodeKey = currentNodeKey[1:]+tuple([newWord])
            else:
                break
            length += 1
        return generatedText


# random.seed("Seinfeld Babey!")
