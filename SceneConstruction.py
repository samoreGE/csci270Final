from MarkovChain import *
from EpisodeGrouper import *

class SceneBuilder:
    def __init__(self, episodes):
        self.episodes = episodes #Should be a list of all episode names
        self.lineChain = MarkovChain(2)
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
            for l in range(len(s.lines) - 1):
                if s.lines[l].type == "line":
                    speaker = s.lines[l].getSceneLineText().split(":")[0]
                    print(speaker)


test = SceneBuilder(["MaleUnbonding", "TheDoorman", "TheExGirlfriend", "TheJacket", "ThePonyRemark", "TheStockTip"])
print("-------------------------------------------------------------------")
test.lineChainBuilder()
