def fixScriptText(filePath):
    linesText = []
    with open(filePath) as file_in:
        compactText = trimWhitespace(file_in)
        for line in compactText:
            print(line)
            splitLine = line.split()
            if isCharLine(splitLine):
                print("CharLine Found!")
                fixedLine = fixCharLine(splitLine)
            else:
                fixedLine = splitLine
            linesText.append(fixedLine)
    outString = ""
    for index in range(len(linesText)):
        if index>0:
            outString+="\n"
        for word in linesText[]
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
    print("fixScripLine(", splitLine, "), len=", len(splitLine))
    if len(splitLine) > 0:
        fixedSplit = [fixLineOpen(splitLine[0])]
        print(fixedSplit)
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




fixScriptText("Scripts/Raw Scripts/TheDoormanRaw.txt")
