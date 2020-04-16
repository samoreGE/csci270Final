def fixScriptText(filePath):
    splitLinesText = []
    with open(filePath) as file_in:
        arrayToFix = rawScriptArray(file_in)
        print(arrayToFix)


def rawScriptArray(scriptFile):
    scriptArray = []
    fullText = ""
    inChunk = True
    for line in scriptFile:
        fullText += line
        for word in line.split():
            if len(line) != 1:
                if word[len(word) - 1] != '\n':
                    scriptArray.append(word)
    print(fullText.split("\n\n"))
    return scriptArray


fixScriptText("Scripts/Raw Scripts/TheDoormanRaw.txt")
