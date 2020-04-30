from EpisodeGrouper import *


def makeScriptFiles(epNames, characters):
    for character in characters:
        makeScriptFileForChar(epNames, character)


def makeScriptFileForChar(epNames, character):
    f = open("Data/" + character + "Lines.txt", "w+")
    for line in getAllCharLines(epNames, character):
        lineToAdd = ""
        for word in line.getChainableSource():
            lineToAdd += " " + word + " "
        f.write(lineToAdd[1:-1] + "\n")


demoNames = ["MaleUnbonding", "TheDoorman", "TheExGirlfriend", "TheJacket", "ThePonyRemark", "TheStockTip"]
charNames = ["jerry", "kramer", "elaine", "george"]

makeScriptFiles(demoNames, charNames)
