def ins2paths(ins):
    paths = []
    for i in range(len(ins)):
        if len(ins[i]['walking']) != 0:
            paths += [ins[i]['walking']['steps'][j]['instruction'] for j in range(len(ins[i]['walking']['steps']))]
        n = len(ins[i]['bus']['buslines'])
        if n != 0:
            paths += ['乘坐 ' + ins[i]['bus']['buslines'][j]['name'] + ' 自 ' + ins[i]['bus']['buslines'][j]['departure_stop']['name'] + ' 至 ' + ins[i]['bus']['buslines'][j]['arrival_stop']['name'] for j in range(n)]
        if ins[i]['railway']['spaces'] != []:
            paths += ['乘坐 ' + ins[i]['railway']['name'] + ' 自 ' + ins[i]['railway']['departure_stop']['name'] + ' 至 ' + ins[i]['railway']['arrival_stop']['name']]
    return paths
