from MarkovChain import *
from SceneConstruction import *
from EpisodeGrouper import *
import random

class EpisodeBuilder:

    def __init__(self, episodes):
        self.episodes = episodes
        self.chains = {}
        self.mainCharacters = {"jerry", "elaine", "george", "kramer"}
        self.suppCharacters = set({})
        self.chainBuilder()

    def chainBuilder(self):
        parsedEpisodes = getEpisodes(self.episodes)
        for e in parsedEpisodes:
            castList = e.getCast()
            for c in castList:
                if c not in self.suppCharacters and c not in self.mainCharacters:
                    self.suppCharacters.add(c)
        for i in self.mainCharacters:
            self.characterChain(i)
        for m in self.suppCharacters:
            self.characterChain(m)

    def characterChain(self, character):
        tempChain = MarkovChain(1)
        characterLines = getAllCharLines(self.episodes, character)
        for line in characterLines:
            tempChain.addData(line.getChainableSource())
        self.chains[character] = tempChain

    def episodeBuilder(self):
        bob = SceneBuilder(self.episodes)
        episode = []
        sceneCount = 3 #Edit this value to reflect how many scenes long you want the episode
        for i in range(sceneCount):
            mainCast = random.sample(self.mainCharacters, random.randint(2, 3))
            suppCast = random.sample(self.suppCharacters, random.randint(0, 2))
            cast = mainCast + suppCast
            cast.append("STAGEDIR")
            print("HELP ME! " + str(cast))
            sequence = bob.sceneGenerate(cast)
            for l in sequence:
                if l is "STAGEDIR":
                    episode.append("STAGEDIR")
                else:
                    episode.append(l.upper() + ": " + self.chains[l].generate())
            episode.append("(Scene end)")
        for m in episode:
            print(m)


test = EpisodeBuilder(["MaleUnbonding", "TheDoorman", "TheExGirlfriend", "TheJacket", "ThePonyRemark", "TheStockTip"])
test.episodeBuilder()




