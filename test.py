import sys
import requests
import datetime
from reflist import ins2paths
import pyttsx3
from PyQt5 import QtWidgets

from gui import Ui_Form

mykey = '39925e5407cbb978492cf5a60911fd10'
url = 'https://restapi.amap.com/v3/place/text?'
url_ip = 'https://restapi.amap.com/v3/ip?parameters'
url_0 = 'https://restapi.amap.com/v3/direction/walking?'
url_1 = 'https://restapi.amap.com/v3/direction/driving?'
url_2 = 'https://restapi.amap.com/v3/direction/transit/integrated?'
url_3 = 'https://restapi.amap.com/v4/direction/bicycling?'
# 感谢高德提供API服务

engine = pyttsx3.init()  # 语音引擎


class mysoft(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super(mysoft, self).__init__()
        self.setupUi(self)

    def statusrefresh(self):  # 刷新按钮状态
        self.label_3.setText('Ready!')
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.label_4.setText('')
        self.label_5.setText('')
        self.label_6.setText('')
        self.label_7.setText('')

    def route(self):  # 路线
        keywords1 = self.lineEdit.text()  # 出发点关键字，多关键字请用“|”分割
        keywords2 = self.lineEdit_2.text()  # 目的地关键字，多关键字请用“|”分割
        global paths  # 路径
        paths = []
        if keywords2 != '':  # 目的地缺省则提示
            if keywords1 == '':  # 出发点缺省则使用当前IP，定位精度为市
                result1 = requests.get(url_ip, {'key': mykey})
                result1 = result1.json()
                result1 = requests.get(url, {'key': mykey, 'keywords': result1['city'], 'city': result1['city']})
                result1 = result1.json()
            else:
                result1 = requests.get(url, {'key': mykey, 'keywords': keywords1})
                result1 = result1.json()
            result2 = requests.get(url, {'key': mykey, 'keywords': keywords2})
            result2 = result2.json()
            if result1['count'] != '0' and result2['count'] != '0':  # 若关键词查询无结果则提示
                self.lineEdit.setText(result1['pois'][0]['name'])
                self.lineEdit_2.setText(result2['pois'][0]['name'])  # 显示查询结果
                location1 = result1['pois'][0]['location']
                location2 = result2['pois'][0]['location']  # 出发点与目的地经纬度
                parameters = {'key': mykey, 'origin': location1, 'destination': location2}
                choice = self.comboBox.currentIndex()  # 交通工具
                if choice == 0:  # 步行
                    routeresult = requests.get(url_0, parameters)
                    routeresult = routeresult.json()
                    if routeresult['status'] == '1':
                        ins = routeresult['route']['paths'][0]['steps']
                        paths = [ins[i]['instruction'] for i in range(len(ins))]
                    self.label_3.setText('info: ' + routeresult['info'])
                elif choice == 1:  # 驾车
                    parameters['originid'] = result1['pois'][0]['id']
                    parameters['destinationid'] = result2['pois'][0]['id']
                    routeresult = requests.get(url_1, parameters)
                    routeresult = routeresult.json()
                    if routeresult['status'] == '1':
                        ins = routeresult['route']['paths'][0]['steps']
                        paths = [ins[i]['instruction'] for i in range(len(ins))]
                    self.label_3.setText('info: ' + routeresult['info'])
                elif choice == 2:  # 公交
                    parameters['city'] = result1['pois'][0]['cityname']
                    parameters['cityd'] = result2['pois'][0]['cityname']
                    parameters['date'] = str(datetime.date.today())
                    routeresult = requests.get(url_2, parameters)
                    routeresult = routeresult.json()
                    if routeresult['status'] == '1':
                        paths = ins2paths(routeresult['route']['transits'][0]['segments'])  # 公交出行返回的路径较复杂，故在函数中实现
                    self.label_3.setText('info: ' + routeresult['info'])
                else:  # 骑行
                    routeresult = requests.get(url_3, parameters)
                    routeresult = routeresult.json()
                    if not routeresult['errcode']:
                        ins = routeresult['data']['paths'][0]['steps']
                        paths = [ins[i]['instruction'] for i in range(len(ins))]
                        self.label_3.setText('info: OK')
                    else:
                        self.label_3.setText('errdetail:' + routeresult['errdetail'])
            else:
                self.label_3.setText('Check the keywords!')
        else:
            self.label_3.setText('Destination is default!')
        if paths:  #若paths不空则可以开始导航（考虑关键词搜索失败，导航规划失败等情况）
            self.pushButton_2.setEnabled(True)

    def navig(self):  # 导航
        self.label_4.setText(paths[0])
        self.pushButton_3.setEnabled(False)
        self.label_5.setText('1')
        self.label_6.setText('/')
        self.label_7.setText(str(len(paths)))
        self.pushButton_2.setEnabled(False)  # pyttsx3若在上一句未结束时开始下一句会出错，下同
        engine.say(paths[0])
        engine.runAndWait()
        self.pushButton_2.setEnabled(True)
        self.pushButton_4.setEnabled(True)

    def before(self):
        n = int(self.label_5.text()) - 1
        self.label_5.setText(str(n))
        self.label_4.setText(paths[n-1])
        engine.say(paths[n-1])
        self.pushButton_2.setEnabled(False)  # pyttsx
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        engine.runAndWait()
        self.pushButton_2.setEnabled(True)
        self.pushButton_4.setEnabled(True)
        if n != 1:
            self.pushButton_3.setEnabled(True)

    def after(self):
        n = int(self.label_5.text())
        self.label_5.setText(str(n+1))
        self.label_4.setText(paths[n])
        engine.say(paths[n])
        self.pushButton_2.setEnabled(False)  # pyttsx
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        engine.runAndWait()
        self.pushButton_2.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        if n+1 != len(paths):
            self.pushButton_4.setEnabled(True)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = mysoft()
    ui.show()
    sys.exit(app.exec_())
