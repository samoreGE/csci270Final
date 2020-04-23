from abc import ABC, abstractmethod


class SceneLine(ABC):

    @abstractmethod
    def getFullLineText(self):
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


class Scene:
    def __init__(self, setting, cast, lines):
        self.setting = setting
        self.cast = cast
        self.lines = lines


class DialogueLine(SceneLine):
    def __init__(self, speaker, lineTextArray):
        self.speaker = speaker
        self.lineTextArray = lineTextArray

    def getFullLineText(self):
        fullLineText = self.speaker + ": ["
        for lineText in self.lineTextArray:
            if isinstance(lineText, LineText):
                fullLineText = fullLineText + "{" + str((lineText.getInlineVal())) + "} "
            else:
                print("FullLine ERROR")
                return " "
        return fullLineText + "]"


class StageDir(SceneLine, LineText):
    def __init__(self, dirText):
        self.dirText = dirText

    def getFullLineText(self):
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
    def __init__(self, wordText):
        self.wordText = wordText

    def getInlineVal(self):
        return self.wordText
