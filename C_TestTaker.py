import random
from C_Test import Question

class TestTaker:
    def __init__(self, traitMeans = [0,0,0], traitsSDs= [1,1,1]):
        self.traitA = random.gauss(traitMeans[0], traitsSDs[0])
        self.traitB = random.gauss(traitMeans[1], traitsSDs[1])
        self.traitC = random.gauss(traitMeans[2], traitsSDs[2])
        self.answers = []
    def takeTest(self, questions):
        ret = []
        for question in questions:
            ret.append(self.useTraitsToAnswerQuestion(question))
        self.answers = ret


    def useTraitsToAnswerQuestion(self, question:Question):
        #returns answers to questions ungraded

        questionTraits = question.arrayForGuessing

        rA = random.gauss(self.traitA,1)
        rB = random.gauss(self.traitB,1)
        rC = random.gauss(self.traitC,1)

        A = 0
        B = 0
        C = 0

        if rA < questionTraits[0]:
            A = 1
        if rB < questionTraits[1]:
            B = 1
        if rC < questionTraits[2]:
            C = 1
        if not A or not B or not C:
            return self.guess(question)
        return question.correct


    def guess(self,question):
        possibleQuesses = question.arrayForGuessing
        while 1:
            g = random.choice(possibleQuesses)
            if random.random()< g:
                ret =  chr(65+possibleQuesses.index(g))
                return ret