def ins2paths(ins):  # 公交paths包括步行部分，非轨道公交部分，轨道交通（含地铁，铁路，高铁等）部分，本函数对其进行分离并存储
    paths = []
    for i in range(len(ins)):
        if ins[i]['walking']:
            paths += [ins[i]['walking']['steps'][j]['instruction'] for j in range(len(ins[i]['walking']['steps']))]
        if ins[i]['bus']['buslines']:
            paths += ['乘坐 ' + ins[i]['bus']['buslines'][0]['name'] + ' 自 ' + ins[i]['bus']['buslines'][0]['departure_stop']['name'] + ' 至 ' + ins[i]['bus']['buslines'][0]['arrival_stop']['name']]
        if ins[i]['railway']['spaces']:
            paths += ['乘坐 ' + ins[i]['railway']['name'] + ' 自 ' + ins[i]['railway']['departure_stop']['name'] + ' 至 ' + ins[i]['railway']['arrival_stop']['name']]
    return paths
