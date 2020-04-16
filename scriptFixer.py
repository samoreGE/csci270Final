def fixScriptText(filePath):
    splitLinesText = []
    with open(filePath) as file_in:
        print(file_in)
        for line in file_in:
            #print(line)
            splitLine = line.split()
            if isCharLine(splitLine):
                #print("CharLine Found!")
                fixedLine = fixCharLine(splitLine)
            else:
                fixedLine = splitLine
            splitLinesText.append(fixedLine)
    outString = splitLineToString(splitLinesText)
    print(outString)


def trimWhitespace(scriptFile):
    trimmedText = []
    for line in scriptFile:
        if len(line) > 1:
            trimmedText.append(line)
    return trimmedText


def isCharLine(splitToTest):
    # ADJUST SCRIPT-BY-SCRIPT
    if len(splitToTest) > 0:
        if splitToTest[0][len(splitToTest[0]) - 1] == ':':
            return True;
    return False


def fixCharLine(splitLine):
    #print("fixScripLine(", splitLine, "), len=", len(splitLine))
    if len(splitLine) > 0:
        fixedSplit = [fixLineOpen(splitLine[0])]
        #print(fixedSplit)
        return fixedSplit
    else:
        print("ERROR PARSING SCRIPTLINE")


def fixLineOpen(firstWord):
    fixedWord = ""
    endChar = firstWord[len(firstWord) - 1]
    fixedWord += firstWord.upper()
    if endChar != ':':
        fixedWord += ":"
    return fixedWord


def splitLineToString(splitLine):
    outString = ""
    for index in range(len(splitLine)):
        if index > 0:
            outString += "\n"
        for index2 in range(len(splitLine[index])):
            if index2 > 0:
                outString += " "
            outString += splitLine[index][index2]
    return outString


fixScriptText("Scripts/Raw Scripts/TheDoormanRaw.txt")