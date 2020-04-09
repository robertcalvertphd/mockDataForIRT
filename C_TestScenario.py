from C_Test import Test
from C_TestTaker import TestTaker
import pandas as pd

class TestScenario:
    def __init__(self, fileName, numberOfQuestions, listOfNbyGroup, traitPrevalence, traitDifficulties, traitDifficultyStandardDeviations):
        self.test = Test(numberOfQuestions, traitDifficulties, traitDifficultyStandardDeviations, traitPrevalence, 0)
        self.testTakers = self.populateTestTakers(listOfNbyGroup)
        self.gradedResponse = self.administerTest(fileName)
        self.createControlFile(fileName)
    def populateTestTakers(self, arrayOfNByGroup, groupMeans = [[0,0,0]], groupSDs = [[1,1,1]]):
        ret = []
        groupID = 0
        for n_of_group in arrayOfNByGroup:
            for i in range(n_of_group):
                ret.append(TestTaker(groupMeans[groupID], groupSDs[groupID]))
            groupID += 1
        return ret
    def administerTest(self, fileName):
        answers = []
        for testTaker in self.testTakers:
            a = testTaker.takeTest(self.test.questions)
            answers.append(a)
            print(sum(a)/len(a))
        df = pd.DataFrame(answers)
        df.to_csv(fileName+".csv")

    def createControlFile(self, fileName):
        ret = []
        for question in self.test.questions:
            ret.append(question.control)
        df = pd.DataFrame(ret)
        df.to_csv(fileName+"_control.csv", index = False, header = None)


TestScenario("f", 100,[1000], [.7,.1,.1], [.5,1,1],[2,1,1]).gradedResponse
