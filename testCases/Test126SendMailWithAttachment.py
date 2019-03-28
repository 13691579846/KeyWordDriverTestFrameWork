from util.ParseExcel import ParseExcel
from config.VarConfig import *
from action.PageAction import *
import traceback
from util.log import Logger
import logging

log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)
p = ParseExcel()
sheetName = p.wb.sheetnames# 获取到excel的所有sheet名称

def Test126MailSendWithAtt():
    try:
        testCasePassNum = 0

        requiredCase = 0
        isExecuteColumnValues = p.getColumnValue(sheetName[0], testCase_testIsExecute)
        # print(columnValues)
        for index, value in enumerate(isExecuteColumnValues):
            # print(index, value)
            # 获取对应的步骤sheet名称
            stepSheetName = p.getCellOfValue(sheetName[0],index+2, testCase_testStepName)
            # print(stepSheetName)
            if value.strip().lower() == 'y':
                requiredCase += 1
                testStepPassNum = 0
                print('开始执行测试用例"{}"'.format(stepSheetName))
                log.logger.info('开始执行测试用例"{}"'.format(stepSheetName))
                # 如果用例被标记为执行y，切换到对应的sheet页
                # 获取对应的sheet表中的总步骤数，关键字，定位方式，定位表达式，操作值
                # 步骤总数
                values = p.getColumnValue(stepSheetName, testStep_testNum) # 第一列数据
                stepNum = len(values)
                print(stepNum)
                for step in range(2, stepNum+2):
                    rawValue = p.getRowValue(stepSheetName, step)
                    # 执行步骤名称
                    stepName = rawValue[testStep_testStepDescribe -2]
                    # 关键字
                    keyWord = rawValue[testStep_keyWord - 2]
                    # 定位方式
                    by = rawValue[testStep_elementBy - 2]
                    # 定位表达式
                    locator = rawValue[testStep_elementLocator - 2]
                    # 操作值
                    operateValue = rawValue[testStep_operateValue - 2]

                    if keyWord and by and locator and operateValue:
                        func = keyWord + '(' +'"' +by +'"'+ ',' +'"'+locator+ '"'+',' +'"'+ operateValue + '"'+')'
                    elif keyWord and by and locator and operateValue is None:
                        func = keyWord + '(' +'"' +by +'"'+ ',' +'"'+locator+ '"'+')'

                    elif keyWord and operateValue and type(operateValue) == str and by is None and locator is None:
                        func = keyWord + '(' +'"' + operateValue + '"' + ')'

                    elif keyWord and operateValue and type(operateValue) == int and by is None and locator is None:
                        func = keyWord + '(' + str(operateValue) +')'

                    else:
                        func = keyWord + '('+')'

                    try:
                        # 执行测试步骤
                        eval(func)
                    except Exception:
                        # 截图
                        picPath = saveScreenShot()
                        # 写回测试结果
                        errorInfo = traceback.format_exc()
                        p.writeTestResult(stepSheetName, step, 'Failed', errorInfo, picPath)
                        print('步骤"{}"执行失败'.format(stepName))
                        log.logger.info('步骤"{}"执行失败'.format(stepName))
                        raise
                    else:
                        print('步骤"{}"执行通过'.format(stepName))
                        log.logger.info('步骤"{}"执行通过'.format(stepName))
                        # 标记测试步骤为pass
                        p.writeTestResult(stepSheetName, step, 'Pass')
                        testStepPassNum += 1
                # print('通过用例步数数:',testStepPassNum)
                if testStepPassNum == stepNum:
                    # 标记测试用例sheet页的执行结果为pass
                    p.writeCell(sheetName[0], index+2, testCase_testResult, 'Pass')
                    testCasePassNum += 1
                else:
                    p.writeCell(sheetName[0], index + 2, testCase_testResult, 'Failed')
        print('共{}条用例，{}条需要被执行，本次执行通过{}条'.format(len(isExecuteColumnValues), requiredCase, testCasePassNum))
        log.logger.info('共{}条用例，{}条需要被执行，本次执行通过{}条'.format(len(isExecuteColumnValues), requiredCase, testCasePassNum))
    except Exception as e:
        print(traceback.format_exc(e))
        log.logger.info(traceback.format_exc(e))

if __name__=='__main__':
    Test126MailSendWithAtt()

