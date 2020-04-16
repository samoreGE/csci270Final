def fixScriptText(filePath):
    with open(filePath) as file_in:
        linesText = ""
        for line in file_in:
            lineText = str(len(line)) + ""
            lineWords = line.split()
            fixScriptLine(lineWords)
            if len(line) > 1:
                endChar = lineWords[0][len(lineWords[0]) - 1]
                print(line)
                print(endChar)
            else:
                print("ERROR: IMPOSSIBLE LINE FORMATTING")
            for index in range(len(lineWords)):
                lineText += lineWords[index] + " "
            linesText += lineText + "\n"
        # print(linesText)


def fixLineOpen(splitLine):
    fixedLine = []
    for index in range(len(splitLine)):
        fixedWord = ""
        startChar = splitLine[index][0]
        endChar = splitLine[index][len(splitLine[index]) - 1]
        if index == 0:
            fixedWord += splitLine[index].upper()
            if endChar != ':':
                fixedWord += ":"
        fixedLine.append(fixedWord)
    return fixedLine


def fixScriptLine(splitLine):
    print("fixScripLine(", splitLine, ")")
    fixedSplit = fixLineOpen(splitLine)
    return fixedSplit


fixScriptText("Scripts/Raw Scripts/TheDoormanRaw.txt")
