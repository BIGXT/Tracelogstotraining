

def createtraceList(arr):
    n=0
    traceidlist=[]
    tracelist= [[]]

    for i in arr:
        if i['traceID'] not in traceidlist:          #建立traceID数组
            traceidlist.append(i['traceID'])

    for j in traceidlist:
        spanlist = []
        tracelist.append([j,])
        for k in arr:
            if k['traceID'] == j:        #别用is，因为内存地址不一样，虽然可能内容相同，毕竟list存的是内存地址而不是数值
                spanlist.append([k['startTime'],k])
        spanlist.sort(key = lambda l:l[0]) #同traceID的span根据开始时间排序
        for m in spanlist:
            tracelist[n + 1].append(m[1])
        n=n+1

    tracelist = [x for x in tracelist if x]
    return tracelist    #返回值为【traceid, 该traceid对应的span】

def getSameTraceidSpan(list):
    a=[[]]
    n=0
    c = 0
    rest_data = []
    for l in list:
        # 删除一行中第c列的值
        rest_l = l[:c]
        rest_l.extend(l[c + 1:])
        # 将删除后的结果加入结果数组
        a.append(rest_l)
    a = [x for x in a if x]
    return a

def listByStartTime(list):
    return list['startTime']

def dataScreening(list, n, st, end):
    #数据筛选，n=0无筛选，n=1删除错误数据,

    if n==0:
        return list
    elif n==1:
        for l in list[:]:
            e = 0
            for r in l:
                for k in r['tags']:
                    if k['key'] == 'error':
                        if k['value'] == 'true':
                            #print(l)
                            e=e+1
                            break
                if e != 0:
                    list.remove(l)
                    l=l
                    break
        return list
    elif n==2:
        for l in list[:]:
            #e = 0
           #l1=0
            for r in l:
                #if l1 == 0:
                #    l1=l1+1
                #    continue
                if r['startTime'] < st or r['startTime'] > end:
                    list.remove(l)
                    #print(l)
                    #e=e+1
                    break
            #if e != 0:
            #    break
        return list

