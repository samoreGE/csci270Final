from MarkovChain import *
from EpisodeGrouper import *

class SceneBuilder:
    def __init__(self, episodes):
        self.episodes = episodes #Should be a list of all episode names
        self.chain = MarkovChain(2)
        self.sceneList = self.readScenes()

    def readScenes(self):
        scenes = []
        episodeList = getEpisodes(self.episodes)
        for i in episodeList:
            for s in i.scenes:
                scenes.append(s)
        return scenes

test = SceneBuilder(["MaleUnbonding", "TheDoorman", "TheExGirlfriend", "TheJacket", "ThePonyRemark", "TheStockTip"])
