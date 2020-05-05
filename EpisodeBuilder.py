from MarkovChain import *
from SceneConstruction import *
from EpisodeGrouper import *
import os
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
        directChain = MarkovChain(2) #Change direction order here
        stageDirections = getAllStageDirs(self.episodes)
        for direction in stageDirections:
            directChain.addData(direction.getChainableSource())
        self.chains["STAGEDIR"] = directChain
        for i in self.mainCharacters:
            self.characterChain(i)
        for m in self.suppCharacters:
            self.characterChain(m)

    def characterChain(self, character):
        tempChain = MarkovChain(3) #Change order here
        characterLines = getAllCharLines(self.episodes, character)
        for line in characterLines:
            tempChain.addData(line.getChainableSource())
        self.chains[character] = tempChain

    def buildScript(self):
        sceneBuilder = SceneBuilder(self.episodes)
        episode = []
        sceneCount = 3 #Edit this value to reflect how many scenes long you want the episode
        episode.append("JERRY: " + self.chains["jerrym"].generate(100))
        for i in range(sceneCount):
            episode.append("[Scene start]")
            mainCast = random.sample(self.mainCharacters, random.randint(2, 3))
            suppCast = random.sample(self.suppCharacters, random.randint(0, 2))
            cast = mainCast + suppCast
            cast.append("STAGEDIR")
            sequence = sceneBuilder.sceneGenerate(cast)
            for l in sequence:
                if l is "STAGEDIR":
                    episode.append("(" + self.chains[l].generate(30)[:-1] + ")")
                else:
                    newLine = self.chains[l].generate(50)
                    newLine = newLine.replace("STAGEDIR", "(" + self.chains["STAGEDIR"].generate(10)[:-1] + ")")
                    episode.append(l.upper() + ": " + newLine)
            episode.append("[Scene end]")
        for line in episode:
            print(line)
        return episode

    def writeEpisode(self, title):
        random.seed(title)
        f = open("Scripts/Bot Scripts/" + title + ".txt", "w+")
        for line in self.buildScript():
            f.write(line.replace(" .", ".").replace(" ?", "?").replace(" !", "!") + '\n')

episodes = []
for fileName in os.listdir("Scripts/Normalized Scripts"):
    if fileName.endswith("Fixed.txt"):
        episodes.append(fileName[:-9])

test = EpisodeBuilder(episodes)
test.writeEpisode("TheCompSciFinal")
