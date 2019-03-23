import sys
import requests
import datetime
from routelist import ins2paths
from PyQt5 import QtWidgets

from gui import Ui_Form

mykey = '39925e5407cbb978492cf5a60911fd10'
url = 'https://restapi.amap.com/v3/place/text?'
url_0 = 'https://restapi.amap.com/v3/direction/walking?'
url_1 = 'https://restapi.amap.com/v3/direction/driving?'
url_2 = 'https://restapi.amap.com/v3/direction/transit/integrated?'
url_3 = 'https://restapi.amap.com/v4/direction/bicycling?'




class mysoft(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super(mysoft, self).__init__()
        self.setupUi(self)

    def statusrefresh(self):
        self.label_3.setText('Ready!')
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.label_4.setText('')
        self.label_5.setText('')
        self.label_6.setText('')
        self.label_7.setText('')

    def route(self):
        keywords1 = self.lineEdit.text()
        keywords2 = self.lineEdit_2.text()
        self.label_3.setText('Searching...')
        self.pushButton.setEnabled(False)
        if keywords2 != '':
            # default location1 will be set by IP in the future
            result1 = requests.get(url, {'key': mykey, 'keywords': keywords1})
            result2 = requests.get(url, {'key': mykey, 'keywords': keywords2})
            result1 = result1.json()
            result2 = result2.json()
            if result1['count'] != '0' and result2['count'] != '0':
                global paths
                self.lineEdit.setText(result1['pois'][0]['name'])
                self.lineEdit_2.setText(result2['pois'][0]['name'])
                location1 = result1['pois'][0]['location']
                location2 = result2['pois'][0]['location']
                parameters = {'key': mykey, 'origin': location1, 'destination': location2}
                choice = self.comboBox.currentIndex()
                if choice == 0:
                    # 步行
                    routeresult = requests.get(url_0, parameters)
                    routeresult = routeresult.json()
                    ins = routeresult['route']['paths'][0]['steps']
                    ins = [ins[i]['instruction'] for i in range(len(ins))]
                    paths = ins
                elif choice == 1:
                    # 驾车
                    parameters['originid'] = result1['pois'][0]['id']
                    parameters['destinationid'] = result2['pois'][0]['id']
                    routeresult = requests.get(url_1, parameters)
                    routeresult = routeresult.json()
                    ins = routeresult['route']['paths'][0]['steps']
                    ins = [ins[i]['instruction'] for i in range(len(ins))]
                    paths = ins
                elif choice == 2:
                    # 公交
                    parameters['city'] = result1['pois'][0]['cityname']
                    parameters['cityd'] = result2['pois'][0]['cityname']
                    parameters['date'] = str(datetime.date.today())
                    routeresult = requests.get(url_2, parameters)
                    routeresult = routeresult.json()
                    ins = routeresult['route']['transits'][0]['segments']
                    paths = ins2paths(ins)

                else:
                    # 骑行
                    routeresult = requests.get(url_3, parameters)
                    routeresult = routeresult.json()
                    ins = routeresult['data']['paths'][0]['steps']
                    ins = [ins[i]['instruction']+'\n' for i in range(len(ins))]
                    paths = ins
                self.label_3.setText('Finished!')
                self.pushButton_2.setEnabled(True)
            else:
                self.label_3.setText('Check the keywords!')
        else:
            self.label_3.setText('Destination is default!')
        self.pushButton.setEnabled(True)

    def navig(self):
        self.label_4.setText(paths[0])
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(True)
        self.label_5.setText('1')
        self.label_6.setText('/')
        self.label_7.setText(str(len(paths)))

    def before(self):
        n = int(self.label_5.text()) - 1
        self.label_5.setText(str(n))
        self.label_4.setText(paths[n-1])
        if n == 1:
            self.pushButton_3.setEnabled(False)
        if n+1 == len(paths):
            self.pushButton_4.setEnabled(True)

    def after(self):
        n = int(self.label_5.text())
        self.label_5.setText(str(n+1))
        self.label_4.setText(paths[n])
        if n+1 == len(paths):
            self.pushButton_4.setEnabled(False)
        if n == 1:
            self.pushButton_3.setEnabled(True)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = mysoft()
    ui.show()
    sys.exit(app.exec_())
