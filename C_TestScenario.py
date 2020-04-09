from C_Test import Test
from C_TestTaker import TestTaker
import pandas as pd

class TestScenario:
    def __init__(self, fileName, numberOfQuestions, listOfNbyGroup, traitPrevalence, traitDifficulties, traitDifficultyStandardDeviations):
        self.test = Test(numberOfQuestions, traitDifficulties, traitDifficultyStandardDeviations, traitPrevalence, 0)
        self.testTakers = self.populateTestTakers(listOfNbyGroup)
        self.administerTest(fileName)
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
            testTaker.takeTest(self.test.questions)
            answers.append(testTaker.answers)

        df = pd.DataFrame(answers)
        df.to_csv(fileName+".csv")
        f = open(fileName + "_xcalibre.txt", "w")
        formatted = format_list_of_lists_for_xCalibre(answers)
        f.write(formatted)
        gradeTests(fileName, self.test.questions, self.testTakers)
    def createControlFile(self, fileName):
        ret = []
        for question in self.test.questions:
            ret.append(question.control)
        df = pd.DataFrame(ret)
        df.to_csv(fileName+"_control.csv", index = False, header = None)

def gradeTests(fileName, questions, testTakers):
    ret = []
    for testTaker in testTakers:
        entry = []
        for i in range(len(questions)):
            if questions[i].correct == testTaker.answers[i]:
                entry.append(1)
            else:
                entry.append(0)
        ret.append(entry)
    df = pd.DataFrame(ret)
    df.to_csv(fileName + "_gradedResponses.csv")


def format_list_of_lists_for_xCalibre(list_of_lists):
    #example format is
    #XXXXXX    information
    #note the space between the two sections must remain consistent.
    id = 0
    ret = ""
    list_of_strings_without_commas = []
    for list in list_of_lists:
        # handle ID
        id += 1
        lengthOfID = str(id).__len__()
        numberOfZeroesAdded = 7-lengthOfID
        idString = ""
        for i in range(numberOfZeroesAdded):
            idString += "0"
        idString += str(id)
        line = "ID" + str(idString) + "   "

        # handle list
        for item in list:
           line+=str(item)
        line += '\n'
        ret+=line
    return ret



TestScenario("f", 100,[1000], [.7,.1,.1], [.5,1,1],[2,1,1])
