from ScriptDataStructure import *


def scriptToEpisodeObj(scriptPath, epName):
    with open(scriptPath) as file_in:
        setting = ""
        sceneLines = []
        episodeScenes = []
        for line in file_in:
            lineText = line.replace("\n", "")
            #print(lineText)
            if lineText[0] == "[":
                if len(sceneLines) > 0:
                    print("Making Scene, setting= " + setting + ", " + str(len(sceneLines)) + " line(s)")
                    episodeScenes.append(Scene(epName, setting, sceneLines))
                    sceneLines = []
                print("SCENE BEGINS")
                if lineText[:9] == "[Setting:":
                    setting = lineText[10:-1]
                print(setting)
            elif lineText[:6] == "(Scene":
                print("SCENE ENDS")
            else:
                newParsedLine = parseLine(splitOnPunct(lineText), epName)
                if isinstance(newParsedLine, SceneLine):
                    sceneLines.append(newParsedLine)
                else:
                    print("LINE TYPE MISMATCH")


def parseLine(lineText, epName):
    if lineText[0] == '(':
        parsedStageDir = parseStageDir(lineText, epName)
        print(parsedStageDir.getSceneLineText())
        return parsedStageDir
    elif lineText.find(':') > -1:
        parsedDiaLine = parseDialogue(lineText, epName)
        print(parsedDiaLine.getSceneLineText())
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


def splitOnPunct(line):
    return line.replace(".", " . ").replace(",", " , ").replace("!", " ! ").replace("?", " ? ").replace('"', " \" ")


scriptToEpisodeObj("Scripts/Normalized Scripts/ThePonyRemarkFixed.txt", "The Pony Remark")
