def ins2paths(ins):
    paths = []
    for i in range(len(ins)):
        if ins[i]['walking']:
            paths += [ins[i]['walking']['steps'][j]['instruction'] for j in range(len(ins[i]['walking']['steps']))]
        if ins[i]['bus']['buslines']:
            paths += ['乘坐 ' + ins[i]['bus']['buslines'][0]['name'] + ' 自 ' + ins[i]['bus']['buslines'][0]['departure_stop']['name'] + ' 至 ' + ins[i]['bus']['buslines'][0]['arrival_stop']['name']]
        if ins[i]['railway']['spaces']:
            paths += ['乘坐 ' + ins[i]['railway']['name'] + ' 自 ' + ins[i]['railway']['departure_stop']['name'] + ' 至 ' + ins[i]['railway']['arrival_stop']['name']]
    return paths


def wait(self):
    self.label_3.setText('Searching...')
