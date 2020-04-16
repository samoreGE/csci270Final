def fixScriptText(filePath):
    splitLinesText = []
    with open(filePath) as file_in:
        arrayToFix = rawScriptArray(file_in)
        print(arrayToFix)


def rawScriptArray(scriptFile):
    scriptArray = []
    for line in scriptFile:
        if len(line) == 1:
            print("ping!")
        else:
            for word in line.split():
                if word[len(word) - 1] == '\n':
                    print("pong!")
                else:
                    scriptArray.append(word)
    return scriptArray





def makeStageDirection(wordArray):
    textOut = ["("]
    for word in wordArray:
        textOut.append(word)
    textOut.append(")")
    return textOut


def makeCharLine(nameArray, lineArray):
    textOut = []
    for word in nameArray:
        textOut.append(word)
    textOut.append(":")
    for word in lineArray:
        textOut.append(word)
    return textOut


def makeSettingLine(settingArray):
    textOut = ["["]
    for word in settingArray:
        textOut.append(word)
    textOut.append("]")
    return textOut


fixScriptText("Scripts/Raw Scripts/TheDoormanRaw.txt")
