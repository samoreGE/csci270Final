def fixScriptText(filePath):
    splitLinesText = []
    with open(filePath) as file_in:
        splitScript = makeSplitScript(file_in)
        print(splitScript)
        for line in splitScript:
            print(line)


def makeSplitScript(scriptFile):
    #CHANGE PER FILE
    scriptArray = []
    fullText = ""
    inChunk = True
    for line in scriptFile:
        fullText += line
    for line in fullText.split("\n\n"):
        scriptArray.append(line.replace('\n', ' '))
    return scriptArray


def detectLineType(lineString):
    #CHANGE PER FILE
    


def makeSettingLine(settingArray):
    textOut = ["SETTING LINE: ["]
    for word in settingArray:
        textOut.append(word)
    textOut.append("] END SETTNG")
    return textOut


def makeStageDirection(wordArray):
    textOut = ["STAGE LINE ("]
    for word in wordArray:
        textOut.append(word)
    textOut.append(") END STAGE")
    return textOut


def makeCharLine(nameArray, lineArray):
    textOut = []
    for word in nameArray:
        textOut.append(word)
    textOut.append(":")
    for word in lineArray:
        textOut.append(word)
    return textOut


fixScriptText("Scripts/Raw Scripts/TheDoormanRaw.txt")
