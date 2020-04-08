from C_Test import Test
from C_TestTaker import TestTaker


class TestScenario:
    def __init__(self, description, numberOfQuestions, listOfNbyGroup, traitPrevalence, traitDifficulties, traitDifficultyStandardDeviations):
        self.test = Test(numberOfQuestions, traitDifficulties, traitDifficultyStandardDeviations, traitPrevalence, 0)
        self.testTakers = self.populateTestTakers(listOfNbyGroup)

    def populateTestTakers(self, arrayOfNByGroup, groupMeans = [[0,0,0]], groupSDs = [[1,1,1]]):
        ret = []
        groupID = 0
        for n_of_group in arrayOfNByGroup:
            for i in range(n_of_group):
                ret.append(TestTaker(groupMeans[groupID], groupSDs[groupID]))
            groupID += 1

    def administerTest(self):
        for testTaker in self.testTakers:
            answers = testTaker.takeTest(self.test.questions)
            print(sum(answers)/len(answers))

t = TestScenario("first test", 100,[1000], [.7,.1,.1], [0,1,1],[1,1,1])
