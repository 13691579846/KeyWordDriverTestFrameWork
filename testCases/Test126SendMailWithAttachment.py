"""
------------------------------------
@Time : 2019/8/3 14:20
@Auth : linux超
@File : Test126SendMailWithAttachment.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
import traceback
import logging

from action.PageAction import *
from config.VarConfig import (
    testCase_testIsExecute,
    testCase_testStepName,
    testStep_testNum,
    testStep_testStepDescribe,
    testStep_keyWord,
    testStep_elementBy,
    testStep_elementLocator,
    testStep_operateValue,
    testCase_testResult
)
from util.log import Logger
from util.ParseExcel import ParseExcel


log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)
p = ParseExcel()
sheetName = p.wb.sheetnames  # 获取到excel的所有sheet名称


def test_126_mail_send_with_att():
    try:
        test_case_pass_num = 0
        required_case = 0
        is_execute_column_values = p.get_column_value(sheetName[0], testCase_testIsExecute)
        print(is_execute_column_values)
        # print(columnValues)
        for index, value in enumerate(is_execute_column_values):
            print(index, value)
            # 获取对应的步骤sheet名称
            step_sheet_name = p.get_cell_of_value(sheetName[0], index + 2, testCase_testStepName)
            print(step_sheet_name)
            if value.strip().lower() == 'y':
                required_case += 1
                test_step_pass_num = 0
                print('开始执行测试用例"{}"'.format(step_sheet_name))
                log.logger.info('开始执行测试用例"{}"'.format(step_sheet_name))
                # 如果用例被标记为执行y，切换到对应的sheet页
                # 获取对应的sheet表中的总步骤数，关键字，定位方式，定位表达式，操作值
                # 步骤总数
                values = p.get_column_value(step_sheet_name, testStep_testNum)  # 第一列数据
                step_num = len(values)
                for step in range(2, step_num + 2):
                    raw_value = p.get_row_value(step_sheet_name, step)
                    # 执行步骤名称
                    step_name = raw_value[testStep_testStepDescribe - 2]
                    # 关键字
                    key_word = raw_value[testStep_keyWord - 2]
                    # 定位方式
                    by = raw_value[testStep_elementBy - 2]
                    # 定位表达式
                    locator = raw_value[testStep_elementLocator - 2]
                    # 操作值
                    operate_value = raw_value[testStep_operateValue - 2]
                    if key_word and by and locator and operate_value:
                        func = \
                            key_word \
                            + '(' + '"' + by + '"' + ',' + '"' + locator + '"' + ',' + '"' + operate_value + '"' + ')'
                    elif key_word and by and locator and operate_value is None:
                        func = \
                            key_word \
                            + '(' + '"' + by + '"' + ',' + '"' + locator + '"' + ')'
                    elif key_word and operate_value and type(operate_value) == str and by is None and locator is None:
                        func = \
                            key_word \
                            + '(' + '"' + operate_value + '"' + ')'
                    elif key_word and operate_value and type(operate_value) == int and by is None and locator is None:
                        func = \
                            key_word \
                            + '(' + str(operate_value) + ')'
                    else:
                        func = \
                            key_word \
                            + '(' + ')'
                    try:
                        # 执行测试步骤
                        eval(func)
                    except Exception:
                        # 截图
                        pic_path = save_screen_shot()
                        # 写回测试结果
                        error_info = traceback.format_exc()
                        p.write_test_result(step_sheet_name, step, 'Failed', error_info, pic_path)
                        print('步骤"{}"执行失败'.format(step_name))
                        log.logger.info('步骤"{}"执行失败'.format(step_name))
                    else:
                        print('步骤"{}"执行通过'.format(step_name))
                        log.logger.info('步骤"{}"执行通过'.format(step_name))
                        # 标记测试步骤为pass
                        p.write_test_result(step_sheet_name, step, 'Pass')
                        test_step_pass_num += 1
                # print('通过用例步数数:',testStepPassNum)
                if test_step_pass_num == step_num:
                    # 标记测试用例sheet页的执行结果为pass
                    p.write_cell(sheetName[0], index + 2, testCase_testResult, 'Pass')
                    test_case_pass_num += 1
                else:
                    p.write_cell(sheetName[0], index + 2, testCase_testResult, 'Failed')
        log.logger.info('共{}条用例，{}条需要被执行，本次执行通过{}条'.
                        format(len(is_execute_column_values), required_case, test_case_pass_num))
    except Exception as e:
        log.logger.info(e)


if __name__ == '__main__':
    test_126_mail_send_with_att()
