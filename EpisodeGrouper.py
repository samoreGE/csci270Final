from ScriptDataStructure import *
from ScriptParser import *


def makeDemo(epNames, character):
    episodes = []
    for name in epNames:
        newEpisodeObject = scriptToEpisodeObj("Scripts/Normalized Scripts/" + name + ".txt", name)
        episodes.append(newEpisodeObject)


makeDemo()