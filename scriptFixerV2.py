def fixScriptText(filePath):
    splitLinesText = []
    with open(filePath) as file_in:
        arrayToFix = rawScriptArray(file_in)
        print(arrayToFix)
        parsedScript = iterateThroughList(arrayToFix)
        print(parsedScript)


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


# 0: Setting Line
# 1: Stage Direction
# 2: Character Line
def iterateThroughList(wordList):
    state = -1
    parsedScript = []
    focusToParse = []
    for index in range(len(wordList)):
        newWord = wordList[index]
        # CHANGE PER FILE
        if len(newWord) < 1:
            print("SOMETHING IS TERRIBLY WRONG")
            break
        if newWord[-1] == ']':
            if state == 0:
                focusToParse.append(newWord[:-1])
            else:
                print("SOMETHING IS TERRIBLY WRONG 2")
        if newWord[0] == '[':
            parsedScript.append(makeLineFromState(focusToParse, state))
            state = 0
            focusToParse.clear()
            focusToParse.append(newWord[1:])
        else:
            focusToParse.append(newWord)
    return parsedScript;


def makeLineFromState(wordArray, state):
    outLine = []
    if state == 0:
        return makeSettingLine(wordArray)
    elif state == 1:
        return makeStageDirection(wordArray)
    elif state == 2:
        nameArray = findNameFromArray(wordArray)
        return makeCharLine(nameArray, wordArray[:len(nameArray)])


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


def findNameFromArray(wordArray):
    # CHANGE PER FILE
    nameArray = []
    for word in wordArray:
        if word[-1] == ':':
            nameArray.append(word[:-1])
            return nameArray
        nameArray.append(word)


fixScriptText("Scripts/Raw Scripts/TheDoormanRaw.txt")
