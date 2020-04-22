from abc import ABC, abstractmethod


class SceneLine(ABC):

    @abstractmethod
    def getText(self):
        pass


class LineText(ABC):
    value = ""

    @abstractmethod
    def getValue(self):
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

    def getText(self):
        return self.lineTextArray


class StageDir(SceneLine, LineText):
    def __init__(self, dirText):
        self.dirText = dirText

    def getText(self):
        return self.dirText

    def getValue(self):
        return self.dirText


class DialogueWord(LineText):
    def __init__(self, wordText):
        self.wordText = wordText

    def getValue(self):
        return self.wordText