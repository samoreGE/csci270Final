from MarkovChain import *
from EpisodeGrouper import *

class SceneBuilder:
    def __init__(self, episodes):
        self.episodes = episodes #Should be a list of all episode names
        self.tempChain = {}
        self.tempKeys = set({})
        self.sceneList = self.readScenes()

    def readScenes(self):
        scenes = []
        episodeList = getEpisodes(self.episodes)
        for i in episodeList:
            for s in i.scenes:
                scenes.append(s)
        return scenes

    def lineChainBuilder(self):
        for s in self.sceneList:
            for l in range(len(s.lines) - 2):
                if s.lines[l].type == "line":
                    speaker1 = s.lines[l].getSceneLineText().split(":")[0]
                else:
                    speaker1 = "STAGEDIR"
                if s.lines[l + 1].type == "line":
                    speaker2 = s.lines[l + 1].getSceneLineText().split(":")[0]
                else:
                    speaker2 = "STAGEDIR"
                if s.lines[l + 2].type == "line":
                    speaker3 = s.lines[l + 2].getSceneLineText().split(":")[0]
                else:
                    speaker3 = "STAGEDIR"
                entry = (speaker3, speaker2, speaker1) #ordered most recent to least recent
                if entry not in self.tempKeys:
                    self.tempKeys.add(entry)
                    self.tempChain[entry] = 0
                self.tempChain[entry] += 1

test = SceneBuilder(["MaleUnbonding", "TheDoorman", "TheExGirlfriend", "TheJacket", "ThePonyRemark", "TheStockTip"])
test.lineChainBuilder()
print(test.tempChain[('elaine', 'jerry', 'elaine')])
