import sys
from PyQt5 import QtWidgets

from gui import Ui_Form
class mysoft(QtWidgets.QMainWindow,Ui_Form):
    def __init__(self):
        super(mysoft, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = mysoft()
    ui.show()
    sys.exit(app.exec_())
