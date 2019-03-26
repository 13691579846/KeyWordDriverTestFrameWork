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

if __name__=='__main__':

    print(projectPath)
    print(exceptionPath)
