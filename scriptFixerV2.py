def fixScriptText(filePath):
    splitLinesText = []
    with open(filePath) as file_in:
        splitScript = makeSplitScript(file_in)
        sortedScript = []
        # print(splitScript)
        for line in splitScript:
            sortedScript.append(makeLineByType(line))
        # print(sortedScript)
        for line in sortedScript:
            print(line)


def makeSplitScript(scriptFile):
    # CHANGE PER FILE
    scriptArray = []
    fullText = ""
    inChunk = True
    for line in scriptFile:
        fullText += line
    for line in fullText.split("\n\n"):
        scriptArray.append(line.replace('\n', ' '))
    return scriptArray


def makeLineByType(lineString):
    print("makeLineByType(" + lineString + ")")
    # CHANGE PER FILE
    if lineString[-1] == ']':
        # print("settingLine!")
        return makeSettingLine(lineString.split("[")[1][:-1])
    elif ':' in lineString:
        # print("charLine!")
        return makeCharLine(lineString.split(':'))
    else:
        # print("stageDirection!")
        return makeStageDirection(lineString.split('(')[1][:-1])


def makeSettingLine(settingArray):
    textOut = "["
    for word in settingArray:
        textOut += word
    textOut += "]"
    return textOut


def makeStageDirection(wordArray):
    textOut = "("
    for word in wordArray:
        textOut += word
    textOut += ")"
    return textOut


def makeCharLine(charLineArray):
    textOut = ""
    for word in charLineArray[0]:
        textOut += word.upper()
    textOut += ":"
    for word in charLineArray[1]:
        textOut += word
    return textOut


<<<<<<< Updated upstream
fixScriptText("Scripts/Raw Scripts/TheBusboyRaw.txt")
=======
fixScriptText("Scripts/Raw Scripts/TheBabyShowerRaw.txt")
>>>>>>> Stashed changes
