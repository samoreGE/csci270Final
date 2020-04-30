from ScriptDataStructure import *
from ScriptParser import *


def getAllCharLines(epNames, character):
    episodes = getEpisodes(epNames)
    allCharLines = []
    for episode in episodes:
        for line in getCharLines(episode, character):
            if isinstance(line, DialogueLine):
                allCharLines.append(line)
    return allCharLines


def getEpisodes(epNames):
    episodes = []
    for name in epNames:
        newEpisodeObject = scriptToEpisodeObj("Scripts/Normalized Scripts/" + name + "Fixed.txt", name)
        if isinstance(newEpisodeObject, Episode):
            episodes.append(newEpisodeObject)
        else:
            print("ERROR: NEW EPISODE NOT MADE")
    return episodes


def getCharLines(episode, character):
    characterLines = []
    for scene in episode.scenes:
        for line in scene.lines:
            if isinstance(line, DialogueLine):
                if line.speaker == character:
                    characterLines.append(line)
    return characterLines


def checkResults(lines, speaker):
    allGood = True
    for line in lines:
        if not isinstance(line, DialogueLine):
            allGood = False
        if not line.speaker == speaker:
            allGood = False
        print(line.getChainableSource())
    if allGood:
        print("All Good!")


demoNames = ["MaleUnbonding", "TheDoorman", "TheExGirlfriend", "TheJacket", "ThePonyRemark", "TheStockTip"]
checkResults(getAllCharLines(demoNames, "george"), "george")
