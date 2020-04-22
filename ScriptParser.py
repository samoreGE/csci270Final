from ScriptDataStructure import *


def scriptToObj(scriptPath):
    with open(scriptPath) as file_in:
        for line in file_in:
            lineText = line.replace("\n", "")
            print(lineText + "(END LINE)")
            parseLine(lineText)


def parseLine(lineText):
    if lineText[0] == '[':
        print("SETTING!")
    elif lineText[0] == '(':
        print("STAGE DIRECTION")
    elif lineText.find(':') > -1:
        print("DIALOGUE")
        parseDialogue(lineText)


def parseDialogue(diaText):
    character = diaText[:diaText.find(':')]
    line = parseDiaLine(diaText[diaText.find(':') + 2:])
    diaLine = DialogueLine(character, line)


def parseDiaLine(diaLine):
    dirText = []
    lineText = []
    inDir = False
    for word in diaLine.split():
        if word[0] == '(':
            print(word+": START OF STAGE DIR")
        if word[-1:] == ')':
            print(word + ": END OF STAGE DIR")
        if not inDir:
            lineText.append(word)
    return []


def getCastFromSegment(segment):
    castList = set()
    for line in segment:
        if isinstance(line, DialogueLine):
            castList.add(line.speaker)
    return castList


scriptToObj("Scripts/Normalized Scripts/ThePonyRemarkFixed.txt")
