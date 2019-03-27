# 存储全局的变量
import os

# 项目根目录
projectPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 截图目录
exceptionPath = projectPath +r'\exceptionpictures'

# 驱动存放路径
iePath = ''
chromePath = ''
fireFox = ''

# excel文件存放路径
excelPath = projectPath + r'\testData\126mailSend.xlsx'

# 测试用例部分列对应的列号
testCase_testCaseName = 2
testCase_testStepName = 4
testCase_testIsExecute = 5
testCase_testRunEndTime = 6
testCase_testResult = 7

# 用例步骤对应的列号
testStep_testNum = 1
testStep_testStepDescribe = 2
testStep_keyWord = 3
testStep_elementBy = 4
testStep_elementLocator = 5
testStep_operateValue = 6
testStep_testRunTime = 7
testStep_testResult = 8
testStep_testErrorInfo = 9
testStep_testErrorPic = 10


if __name__=='__main__':

    print(projectPath)
    print(exceptionPath)
