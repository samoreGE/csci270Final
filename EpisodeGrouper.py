from ScriptDataStructure import *
from ScriptParser import *


def makeDemo(epNames, character):
    episodes = getEpisodes(epNames)
    for episode in episodes:
        getCharLines(episodes, character)

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
    for scene in episode.scenes:
        if isinstance(scene, Scene):
            for line in scene:
                if isinstance(line, DialogueLine):
                    
                elif not isinstance(line, StageDir):
                    print("ERROR: NEW EPISODE NOT MADE")
        else:
            print("ERROR: NON-SCENE FOUND IN EPISODE")


demoNames = ["MaleUnbonding", "TheDoorman", "TheExGirlfriend", "TheJacket", "ThePonyRemark", "TheStockTip"]
makeDemo(demoNames, "jerry")