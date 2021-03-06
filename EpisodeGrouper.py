from ScriptParser import *


def getAllCharLines(epNames, character):
    episodes = getEpisodes(epNames)
    allCharLines = []
    for episode in episodes:
        for line in getCharLines(episode, character):
            if isinstance(line, DialogueLine):
                allCharLines.append(line)
        print("Ep Name: " + episode.title + ", cast:" + str(episode.getCast()))
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


def getAllStageDirs(epNames):
    episodes = getEpisodes(epNames)
    allStageDirs = []
    for episode in episodes:
        for line in getStagDirs(episode):
            allStageDirs.append(line)
    return allStageDirs


def getStagDirs(episode):
    stageDirs = []
    for scene in episode.scenes:
        for line in scene.lines:
            if isinstance(line, StageDir):
                stageDirs.append(line)
            elif isinstance(line, DialogueLine):
                for word in line.lineTextArray:
                    if isinstance(word, DialogueLine):
                        stageDirs.append(line)
    return stageDirs


def getCharLines(episode, character):
    characterLines = []
    for scene in episode.scenes:
        for line in scene.lines:
            if isinstance(line, DialogueLine):
                if line.speaker == character:
                    characterLines.append(line)
    return characterLines


def checkResults(lines, speaker):
    print("Checking results...")
    allGood = True
    for line in lines:
        if not isinstance(line, DialogueLine):
            allGood = False
        if not line.speaker == speaker:
            allGood = False
        # print(line.getChainableSource())
    if allGood:
        print("All Good!")
    return allGood
