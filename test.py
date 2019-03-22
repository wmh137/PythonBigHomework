import sys
import requests
from PyQt5 import QtWidgets

from gui import Ui_Form

mykey = '39925e5407cbb978492cf5a60911fd10'
url = 'https://restapi.amap.com/v3/place/text?'

class mysoft(QtWidgets.QMainWindow,Ui_Form):
    def __init__(self):
        super(mysoft, self).__init__()
        self.setupUi(self)
    def route(self):
        keywords1 = self.lineEdit.text()
        keywords2 = self.lineEdit_2.text()
        result1 = requests.get(url, {'key': mykey, 'keywords': keywords1})
        result2 = requests.get(url, {'key': mykey, 'keywords': keywords2})
        result1 = result1.json()
        result2 = result2.json()
        self.lineEdit.setText(result1['pois'][0]['name'])
        self.lineEdit_2.setText(result2['pois'][0]['name'])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = mysoft()
    ui.show()
    sys.exit(app.exec_())
