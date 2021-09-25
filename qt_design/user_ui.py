import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic


form_class = uic.loadUiType("user_ui.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.rviz_btn.clicked.connect(self.launch_rviz)
        self.move_base_btn.clicked.connect(self.launch_move_base)
        self.lotti1_btn.clicked.connect(self.launch_lotti)

        self.pkg_name = "lotti_nav"
        self.rviz_name = "rviz"
        self.move_base_name = "move_base"
        self.lotti_name = "lotti"

    def launch(self, file_name):
        import subprocess
        subprocess.Popen(["roslaunch", f"{self.pkg_name}", f"{file_name}.launch"])

    def launch_rviz(self):
        self.launch("rviz")

    def launch_move_base(self):
        self.launch("move_base")

    def launch_lotti(self):
        self.launch("lotti_operate")

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()

    app.exec_()