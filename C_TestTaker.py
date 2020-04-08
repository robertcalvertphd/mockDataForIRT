import random


class TestTaker:
    def __init__(self, traitMeans = [0,0,0], traitsSDs= [1,1,1]):
        self.traitA = random.gauss(traitMeans[0], traitsSDs[0])
        self.traitB = random.gauss(traitMeans[1], traitsSDs[1])
        self.traitC = random.gauss(traitMeans[2], traitsSDs[2])

    def takeTest(self, questions):
        ret = []
        for question in questions:
            ret.append(self.useTraitsToAnswerQuestion(question.traits))

    def useTraitsToAnswerQuestion(self, questionTraits):
        rA = self.traitA
        rB = self.traitB
        rC = self.traitC

        if rA < questionTraits[0]:
            A = True
        if rB < questionTraits[1]:
            B = True
        if rC < questionTraits[2]:
            C = True
        if not A or not B or not C:
            return False
        return True
