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
    


fixScriptText("Scripts/Raw Scripts/TheDoormanRaw.txt")
