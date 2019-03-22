import sys
import requests
from PyQt5 import QtWidgets

from gui import Ui_Form

mykey = '39925e5407cbb978492cf5a60911fd10'
url = 'https://restapi.amap.com/v3/place/text?'
url_0 = 'https://restapi.amap.com/v3/direction/walking?'
url_1 = 'https://restapi.amap.com/v3/direction/driving?'
url_2 = 'https://restapi.amap.com/v3/direction/transit/integrated?'
url_3 = 'https://restapi.amap.com/v4/direction/bicycling'


class mysoft(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super(mysoft, self).__init__()
        self.setupUi(self)

    def statusready(self):
        self.label_3.setText('Ready!')

    def route(self):
        self.label_3.setText('Searching...')
        keywords1 = self.lineEdit.text()
        keywords2 = self.lineEdit_2.text()
        if keywords2 != '':
            # default location1 will be set by IP in the future
            result1 = requests.get(url, {'key': mykey, 'keywords': keywords1})
            result2 = requests.get(url, {'key': mykey, 'keywords': keywords2})
            result1 = result1.json()
            result2 = result2.json()
            if result1['count'] != '0' and result2['count'] != '0':
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
                elif choice == 1:
                    # 驾车
                    parameters['originid'] = result1['pois'][0]['id']
                    parameters['destinationid'] = result2['pois'][0]['id']
                    routeresult = requests.get(url_1, parameters)
                    routeresult = routeresult.json()
                    ins = routeresult['route']['paths'][0]['steps']
                    ins = [ins[i]['instruction'] for i in range(len(ins))]
                elif choice == 2:
                    # 公交
                    parameters['city'] = result1['pois'][0]['cityname']
                    parameters['cityd'] = result2['pois'][0]['cityname']
                    routeresult = requests.get(url_2, parameters)
                    routeresult = routeresult.json()
                    ins = routeresult['route']['transits'][0]['segments']
                    ins_departure = [ins[i]['bus']['busliness']['departure_stop']['name'] for i in range(len(ins))]
                    ins_arrival = [ins[i]['bus']['busliness']['arrival_stop']['name'] for i in range(len(ins))]
                    ins_stop = [ins[i]['bus']['busliness']['name'] for i in range(len(ins))]
                else:
                    # 骑行
                    routeresult = requests.get(url_3, parameters)
                    routeresult = routeresult.json()
                    ins = routeresult['data']['paths'][0]['steps']
                    ins = [ins[i]['instruction'] for i in range(len(ins))]
                self.label_3.setText('Finished!')
            else:
                self.label_3.setText('Check the keywords!')
        else:
            self.label_3.setText('Destination is default!')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = mysoft()
    ui.show()
    sys.exit(app.exec_())
