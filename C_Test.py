import random

class Test:
    def __init__(self, n, difficultyByTrait, sdOfTraitDifficulty, pOfTraits, pLinkedTo):
        pm = [n,difficultyByTrait,sdOfTraitDifficulty,pOfTraits, 4, pLinkedTo]
        self.questions = self.createQuestions(pm)

    def createQuestions(self, pm):
        ret = []
        for i in range(pm[0]):
            ret.append(Question(i+1,pm[1],pm[2],pm[3],pm[4]))
        return ret

class Question:
    def __init__(self, id, traits, sd_traits, pTraits, numberOfOptions = 4, unbalancedGuessing = True, linkedTo=False):
        self.traits = traits #  traits should have ridiculously high values if they are not relevant.
        self.sd_traits = sd_traits
        self.pTraits = pTraits
        self.linkedTo = linkedTo
        self.numberOfOptions = numberOfOptions
        self.correct = chr(random.randint(1,numberOfOptions)+64)
        self.arrayForGuessing = []
        guessWeight = []
        for i in range(numberOfOptions):
            if unbalancedGuessing:
                guessWeight.append(random.randint(1,10))
            else:
                guessWeight.append(1)
        for weight in guessWeight:
            self.arrayForGuessing.append(weight/sum(guessWeight))
        self.control = [id,self.correct, self.numberOfOptions, 1, 'Y', 'M']

        # linkedTo is an array of tuples that are associated with this question of form (p,id)
        # where p is probability of getting this question correct if id was correct


