from abc import ABC, abstractmethod


class Chainable(ABC):

    @abstractmethod
    def getChainableSource(self):
        pass


class SceneLine(ABC):

    @abstractmethod
    def getSceneLineText(self):
        pass


class LineText(ABC):
    value = ""

    @abstractmethod
    def getInlineVal(self):
        pass


class Episode:
    def __init__(self, title, scenes):
        self.title = title
        self.scenes = scenes


class Scene(Chainable):
    def __init__(self, epTitle, setting, lines):
        self.epTitle = epTitle
        self.setting = setting
        self.lines = lines

    def getCast(self):
        castList = set()
        for line in self.lines:
            if isinstance(line, DialogueLine):
                castList.add(line.speaker)
        return castList


class DialogueLine(SceneLine, Chainable):

    def __init__(self, epTitle, speaker, lineTextArray):
        self.epTitle = epTitle
        self.speaker = speaker
        self.lineTextArray = lineTextArray

    def getSceneLineText(self):
        fullLineText = self.speaker + ": ["
        for lineText in self.lineTextArray:
            if isinstance(lineText, LineText):
                fullLineText = fullLineText + "{" + str((lineText.getInlineVal())) + "} "
            else:
                print("FullLine ERROR")
                return " "
        return fullLineText + "]"

    def getChainableSource(self):
        chainableSourceOut = []
        for lineText in self.lineTextArray:
            if isinstance(lineText, SingleWord):
                chainableSourceOut.append(SingleWord.getInlineVal())
            else:
                chainableSourceOut.append(SingleWord(self.epTitle, "STAGEDIR"))
        return chainableSourceOut


class StageDir(SceneLine, LineText, Chainable):
    def __init__(self, epTitle, dirText):
        self.epTitle = epTitle
        self.dirText = dirText

    def getSceneLineText(self):
        return self.dirTextToString()

    def getInlineVal(self):
        return self.dirTextToString()

    def dirTextToString(self):
        dirTextString = "DIR: "
        for dirWord in self.dirText:
            if isinstance(dirWord, SingleWord):
                dirTextString = dirTextString + "{" + str(dirWord.getInlineVal()) + "}" + ' '
            else:
                print("DirText ERROR")
                return " "
        return dirTextString[:-1]


class SingleWord(LineText):
    def __init__(self, epTitle, word):
        self.epTitle = epTitle
        self.word = word

    def getInlineVal(self):
        return self.word
