from ScriptDataStructure import *


def scriptToObj(scriptPath):
    with open(scriptPath) as file_in:
        for line in file_in:
            lineText = line.replace("\n", "")
            # print(lineText + "(END LINE)")
            parseLine(splitOnPunct(lineText))


def parseLine(lineText):
    if lineText[0] == '[':
        print("SETTING!")
    elif lineText[0] == '(':
        print("STAGE DIRECTION")
    elif lineText.find(':') > -1:
        print("DIALOGUE")
        parsedDiaLine = parseDialogue(lineText)
        print(parsedDiaLine.getFullLineText())


def parseDialogue(diaText):
    character = diaText[:diaText.find(':')]
    line = parseDiaLine(diaText[diaText.find(':') + 2:])
    diaLine = DialogueLine(character, line)
    return diaLine


def parseDiaLine(diaLine):
    dirText = []
    lineText = []
    inDir = False
    for word in diaLine.split():
        if not inDir:
            if word[0] == '(':
                inDir = True
                if word[-1:] == ')':
                    dirText.append(SingleWord(word[1:-1]))
                    lineText.append(StageDir(dirText))
                    inDir = False
                    dirText = []
                else:
                    dirText.append(SingleWord(word[1:]))
            else:
                lineText.append(SingleWord(word))
        else:
            if word[-1:] == ')':
                dirText.append(SingleWord(word[:-1]))
                lineText.append(StageDir(dirText))
                inDir = False
                dirText = []
            else:
                dirText.append(SingleWord(word))

    return lineText


def splitOnPunct(line):
    return line.replace(".", " . ").replace(",", " , ").replace("!", " ! ").replace("?", " ? ")


def getCastFromSegment(segment):
    castList = set()
    for line in segment:
        if isinstance(line, DialogueLine):
            castList.add(line.speaker)
    return castList


scriptToObj("Scripts/Normalized Scripts/TheStockTipFixed.txt")
