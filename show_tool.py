# 作者：东东

import sys
from PyQt5 import QtWidgets
import subprocess
from untitled import Ui_Form
import tkinter as tk
from tkinter import filedialog

class MyPyQT_Form(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(MyPyQT_Form, self).__init__()
        self.setupUi(self)

    # 检查连接是否成功
    def button1(self):
        devices = 'adb devices'
        d = subprocess.getstatusoutput(devices)
        if d[1] == "List of devices attached\n":
            self.textEdit.setText("连接失败，请检查是否开启usb调试和传输文件")
        else:
            self.textEdit.setText(subprocess.getoutput(devices))

    # 输出日志
    def button2(self):
        log = f'adb logcat -v time -d>d:/{self.lineEdit.text()}.log'
        logcat = subprocess.getstatusoutput(log)
        if logcat[0] == 0 :
            self.textEdit.setText("已成功输出日志 \n"f"路径：代理测试工具路径下的{self.lineEdit.text()}.log")
        elif subprocess.getoutput(log) == "拒绝访问。":
            self.textEdit.setText("输出失败，请确定手机是否连接成功")
        else:
            self.textEdit.setText(subprocess.getoutput(log))

    # 工具使用说明
    def button3(self):
        help = "[需要按照步骤来，不然可能出现无响应！！！]\n\n"\
               "1.点击连接手机，提示xxxxx device，表示连接成功 \n\n"\
               "2.全局日志：连接成功后，输入生成log文件的名字，点击输出全局日志 \n\n" \
               "3.局部日志：连接成功后，调整需要生成的日志从什么时间段开始，然后输入生成log文件的名字，点击输出局部日志 \n\n" \
               "[安装和卸载都需要连接手机成功才能进行！！！]\n\n"\
               "4.安装功能，右方直接点击导入apk，选择想要安装的apk，然后导入进行安装就好了，安装时可能会卡一下，需要稍等一小会~\n\n"\
               "5.卸载填写的是包体的包名，比如：com.netease.newsreader.activity"
        self.textEdit.setText(help)

    # 安装包体
    def install(self):
        it = f"adb install -r {self.lineEdit_2.text()}"
        installs = subprocess.getoutput(it)
        self.textEdit.setText(installs)

    # 卸载包体
    def uninstall(self):
        unit = f"adb uninstall {self.lineEdit_3.text()}"
        uninstalls = subprocess.getoutput(unit)
        self.textEdit.setText(uninstalls)

    # 获取包体路径
    def get_apk(self):
        root = tk.Tk()
        root.withdraw()
        Filepath = filedialog.askopenfilename()
        self.lineEdit_2.setText(Filepath)

    # 获取局部日志
    def get_timelog(self):
        data = self.datetime.text()
        print(data)
        log = f'adb logcat -t "{data}.0000">d:{self.lineEdit.text()}.log'
        logcat = subprocess.getstatusoutput(log)
        if logcat[0] == 0 :
            self.textEdit.setText("已成功输出日志 \n"f"路径：代理测试工具路径下的{self.lineEdit.text()}.log")
        elif subprocess.getoutput(log) == "拒绝访问。":
            self.textEdit.setText("输出失败，请确定手机是否连接成功")
        else:
            self.textEdit.setText(subprocess.getoutput(log))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    sys.exit(app.exec_())

