from EpisodeGrouper import *
from os import listdir


def getCharLinesFromFile(fileName):
    allCharLines = []
    with open("Data/"+fileName) as file_in:
        for line in file_in:
            epName = line[line.find("(")+1:line.find(")")]
            wordArray = []
            for word in line.split():
                wordArray.append(SingleWord(epName, word))
            allCharLines.append(DialogueLine(epName, fileName[6:-4], wordArray))
    return allCharLines


def makeCharLineFiles(epNames, characters):
    for character in characters:
        makeScriptFileForChar(epNames, character)


def makeScriptFileForChar(epNames, character):
    f = open("Data/Lines_" + character + ".txt", "w+")
    for line in getAllCharLines(epNames, character):
        lineToAdd = ""
        for word in line.getChainableSource():
            lineToAdd += " " + word + " "
        f.write("(" + line.epTitle+") "+lineToAdd[1:-1] + "\n")


demoNames = ["MaleUnbonding", "TheDoorman", "TheExGirlfriend", "TheJacket", "ThePonyRemark", "TheStockTip"]
charNames = ["jerry", "kramer", "elaine", "george"]

makeCharLineFiles(demoNames, charNames)
for data in listdir("Data/"):
    getCharLinesFromFile(data)
