from ScriptDataStructure import *


def scriptToEpisodeObj(scriptPath, epName):
    with open(scriptPath) as file_in:
        setting = ""
        sceneLines = []
        episodeScenes = []
        for line in file_in:
            lineText = line.replace("\n", "").lower()
            if lineText[0] == "[":
                if len(sceneLines) > 0:
                    newScene = Scene(epName, setting, sceneLines)
                    # print("New Scene, setting: " + setting + ", " + str(len(sceneLines)) + " line(s), cast: " + str(newScene.getCast()))
                    episodeScenes.append(newScene)
                    sceneLines = []
                if lineText[:9] == "[setting:":
                    setting = lineText[10:-1]
            elif lineText[:6] != "(scene":
                newParsedLine = parseLine(
                    lineText.replace(".", " . ").replace(",", " , ").replace("!", " ! ").replace("?", " ? ").replace(
                        '"', " \" "), epName)
                if isinstance(newParsedLine, SceneLine):
                    sceneLines.append(newParsedLine)
                else:
                    print("LINE TYPE MISMATCH")
        # print("New Episode, name: " + epName + ", scene count: " + str(len(episodeScenes)))
        return Episode(epName, episodeScenes)


def parseLine(lineText, epName):
    if lineText[0] == '(':
        parsedStageDir = parseStageDir(lineText, epName)
        #        print(parsedStageDir.getSceneLineText())
        return parsedStageDir
    elif lineText.find(':') > -1:
        parsedDiaLine = parseDialogue(lineText, epName)
        #        print(parsedDiaLine.getSceneLineText())
        return parsedDiaLine


def parseStageDir(lineText, epName):
    trimmedSplitDir = lineText[1:-1].split()
    dirText = []
    for word in trimmedSplitDir:
        dirText.append(SingleWord(epName, word))
    return StageDir(epName, dirText)


def parseDialogue(diaText, epName):
    character = diaText[:diaText.find(':')]
    line = parseDiaLine(diaText[diaText.find(':') + 2:], epName)
    diaLine = DialogueLine(epName, character, line)
    return diaLine


def parseDiaLine(diaLine, epName):
    dirText = []
    lineText = []
    inDir = False
    for word in diaLine.split():
        if not inDir:
            if word[0] == '(':
                inDir = True
                if word[-1:] == ')':
                    if len(word[1:-1]) != 0:
                        dirText.append(SingleWord(epName, word[1:-1]))
                    lineText.append(StageDir(epName, dirText))
                    inDir = False
                    dirText = []
                else:
                    dirText.append(SingleWord(epName, word[1:]))
            else:
                lineText.append(SingleWord(epName, word))
        else:
            if word[-1:] == ')':
                if len(word[:-1]) != 0:
                    dirText.append(SingleWord(epName, word[:-1]))
                lineText.append(StageDir(epName, dirText))
                inDir = False
                dirText = []
            else:
                dirText.append(SingleWord(epName, word))
    return lineText
