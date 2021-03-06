from abc import ABC, abstractmethod


class Chainable(ABC):

    @abstractmethod
    def getChainableSource(self):
        pass


class Keyable(ABC):

    @abstractmethod
    def getKeyVer(self):
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


class Episode(Chainable):
    def __init__(self, title, scenes):
        self.title = title
        self.scenes = scenes

    def getCast(self):
        castList = set()
        for scene in self.scenes:
            for char in scene.getCast():
                castList.add(char)
        return castList

    def getChainableSource(self):
        chainableSourceOut = []
        return chainableSourceOut


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

    def getChainableSource(self):
        chainableSourceOut = []
        for lineText in self.lineTextArray:
            chainableSourceOut.append(lineText.getKeyVer())
        return chainableSourceOut


class DialogueLine(SceneLine, Chainable, Keyable):

    def __init__(self, epTitle, speaker, lineTextArray):
        self.type = "line"
        self.epTitle = epTitle
        self.speaker = speaker
        self.lineTextArray = lineTextArray

    def getSceneLineText(self):
        fullLineText = self.speaker + ": "
        for lineText in self.lineTextArray:
            if isinstance(lineText, LineText):
                fullLineText = fullLineText + str(lineText.getInlineVal()) + " "
            else:
                print("FullLine ERROR")
                return " "
        return fullLineText

    def getChainableSource(self):
        chainableSourceOut = []
        for lineText in self.lineTextArray:
            chainableSourceOut.append(lineText.getKeyVer())
        return chainableSourceOut

    def getKeyVer(self):
        return self.speaker


class StageDir(SceneLine, LineText, Chainable, Keyable):
    def __init__(self, epTitle, dirText):
        self.type = "direction"
        self.epTitle = epTitle
        self.dirText = dirText

    def getSceneLineText(self):
        return self.dirTextToString()

    def getInlineVal(self):
        return self.dirTextToString()

    def getChainableSource(self):
        chainableSourceOut = []
        for dirWord in self.dirText:
            chainableSourceOut.append(dirWord.getKeyVer())
        return chainableSourceOut

    def dirTextToString(self):
        dirTextString = "("
        for dirWord in self.dirText:
            if isinstance(dirWord, SingleWord):
                dirTextString = dirTextString + str(dirWord.getInlineVal()) + ' '
            else:
                print("DirText ERROR")
                return " "
        return dirTextString[:-1] + ")"

    def getKeyVer(self):
        return "STAGEDIR"


class SingleWord(LineText, Keyable):
    def __init__(self, epTitle, word):
        self.epTitle = epTitle
        self.word = word

    def getInlineVal(self):
        return self.word

    def getKeyVer(self):
        return self.getInlineVal()
