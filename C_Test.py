class Test:
    def __init__(self, n, difficultyByTrait, sdOfTraitDifficulty, pOfTraits, pLinkedTo):
        pm = [n,difficultyByTrait,sdOfTraitDifficulty,pOfTraits, pLinkedTo]
        self.questions = self.createQuestions(pm)

    def createQuestions(self, pm):
        ret = []
        for i in range(pm[0]):
            ret.append(Question(pm[1],pm[2],pm[3],pm[4],pm[5],pm[6]))
        return ret

class Question:
    def __init__(self, traits, exclusionary=False, linkedTo=False):
        self.traits = traits #  traits should have ridiculously high values if they are not relevant.
        self.exclusionary = exclusionary
        self.linkedTo = linkedTo

        # linkedTo is an array of tuples that are associated with this question of form (p,id)
        # where p is probability of getting this question correct if id was correct


