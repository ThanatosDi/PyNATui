import json
import os
import sys

from pynat import get_ip_info
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox

from PyNAT import Ui_PyNAT
from PyNAT_Setting import Ui_PyNAT_Setting


class PyNAT_Setting(QDialog):
    def __init__(self):
        super().__init__()
        self.setting = Ui_PyNAT_Setting()
        self.setting.setupUi(self)
        self.show()
        with open('setting.json','r+',encoding='utf-8') as setting:
            self.SettingData = json.load(setting)
        #事件處理
        self.setting.CancelButton.clicked.connect(self.close)
        self.setting.SaveButton.clicked.connect(self.SaveButton)
        self.setting.SourcePortInput.setText(str(self.SettingData['setting']['source_port']))
    
    def SaveButton(self):
        """保存資料"""
        with open('setting.json','w',encoding='utf-8') as w:
            Data = {'setting':{'source_port':int(self.setting.SourcePortInput.text())}}
            json.dump(Data, w, ensure_ascii=False, sort_keys=True)
        self.close()



class PyNAT(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_PyNAT()
        self.ui.setupUi(self)
        self.show()
        if not os.path.exists('setting.json'):
            with open('setting.json','w+',encoding='utf-8') as w:
                Data = {'setting':{'source_port':54320}}
                json.dump(Data, w, ensure_ascii=False, sort_keys=True)
        with open('setting.json','r+',encoding='utf-8') as setting:
            self.SettingData = json.load(setting)
        #事件處理
        self.ui.CheckButton.clicked.connect(self.CheckButton_Click)
        self.ui.ShutdownButton.clicked.connect(self.close)
        self.ui.SettingButton.clicked.connect(self.SettingButton_Click)


    #事件
    def CheckButton_Click(self):
        """檢測"""
        with open('setting.json','r+',encoding='utf-8') as setting:
            self.SettingData = json.load(setting)
        self.ui.NAT_input.setText('')
        self.ui.Internal_input.setText('')
        self.ui.External_input.setText('')
        self.ui.progressBar.setProperty("value", 0)
        topology, ext_ip, ext_port, int_ip = get_ip_info(include_internal=True,source_port=self.SettingData['setting']['source_port'])
        self.ui.progressBar.setProperty("value", 50)
        self.ui.NAT_input.setText(topology)
        self.ui.Internal_input.setText(f'{int_ip}:{ext_port}')
        self.ui.External_input.setText(f'{ext_ip}:{ext_port}')
        self.ui.progressBar.setProperty("value", 100)

    def SettingButton_Click(self):
        """設定"""
        self.setting = PyNAT_Setting()
        self.setting.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    w = PyNAT()
    w.show()
    sys.exit(app.exec_())