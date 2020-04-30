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
        if isinstance(scene, Scene):
            for line in scene.lines:
                if isinstance(line, DialogueLine):
                    if line.speaker == character:
                        characterLines.append(line)
                elif not isinstance(line, StageDir):
                    print("ERROR: NEW EPISODE NOT MADE")
        else:
            print("ERROR: NON-SCENE FOUND IN EPISODE")
    return characterLines


demoNames = ["MaleUnbonding", "TheDoorman", "TheExGirlfriend", "TheJacket", "ThePonyRemark", "TheStockTip"]
getAllCharLines(demoNames, "jerry")
