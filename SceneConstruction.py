from MarkovChain import *
from EpisodeGrouper import *

class SceneBuilder:
    def __init__(self, episodes):
        self.episodes = episodes #Should be a list of all episode names
        self.tempChain = {}
        self.tempKeys = set({})
        self.sceneList = self.readScenes()
        self.lineChainBuilder()

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
                entry = (speaker1, speaker2) #ordered most recent to least recent
                if entry not in self.tempKeys:
                    self.tempKeys.add(entry)
                    self.tempChain[entry] = {}
                    self.tempChain[entry]['entrySet'] = set({})
                if speaker3 not in self.tempChain[entry]['entrySet']:
                    self.tempChain[entry]['entrySet'].add(speaker3)
                    self.tempChain[entry][speaker3] = 0
                self.tempChain[entry][speaker3] += 1

    def sceneGenerate(self, cast):
        map = {}
        for i in cast:
            for l in cast:
                count = 0
                if (i,l) in self.tempChain.keys():
                    for m in cast:
                        if m in self.tempChain[(i,l)]:
                            count += self.tempChain[(i,l)][m]
                            map[(i,l)] = {}
                    for m in cast:
                        if m in self.tempChain[(i,l)]:
                            map[(i,l)][m] = (self.tempChain[(i,l)][m])/count
        print(map)
        return self.generate(map)

    #The following two function were taken directly from Dr. Goadrich's in-class Markov chain code, although the
    #generate function has been modified
    def generate(self, mc):
        current = list(random.choice(list(mc.keys())))
        print(current)
        seq = []
        for i in range(30):
            seq.append(self.discrete_prob(mc[tuple(current)]))
            current = current[1:] + [seq[-1]]
            if current not in list(mc.keys()):
                current = list(random.choice(list(mc.keys())))
        newSeq = []
        for i in range(len(seq) - 1):
            if i == 0:
                if seq[0] != seq[1]:
                    newSeq.append(seq[0])
                    newSeq.append(seq[1])
                else:
                    newSeq.append(seq[0])
            else:
                if seq[i] != seq[i + 1]:
                    newSeq.append(seq[i + 1])
        return newSeq

    def discrete_prob(self, d):
        r = random.random()
        sum = 0
        for k in d:
            sum += d[k]
            if r < sum:
                return k

test = SceneBuilder(["MaleUnbonding", "TheDoorman", "TheExGirlfriend", "TheJacket", "ThePonyRemark", "TheStockTip"])
test.sceneGenerate(['jerry', 'george', 'doorman 2', 'STAGEDIR'])

