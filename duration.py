import hashlib
import numpy as np

import creattraceList
import file


def getDurationList(arr):
    svcName1=''
    svcName2=''
    traceId=0
    spanId1=0
    spanId2=0
    duration=0
    n=0
    duartionlist= [[]]

    for i in arr:
        for j in i:
            if j['references'] == []:
                continue
            elif j['references'][0]["refType"] == 'CHILD_OF':          #建立traceID数组
                svcName2=j['process']['serviceName']
                duration=j['duration']
                spanId2=j['spanID']
                traceId=j['traceID']
                n=n+1
                for i in arr:
                    if i[0]['traceID'] == j['references'][0]["traceID"]:
                        for k in i:
                            if k['spanID'] == j['references'][0]["spanID"]:
                                svcName1 = k['process']['serviceName']
                                spanId1=k['spanID']
#                               s=[]
#                               s.append(svcName1)
#                               s.append(svcName2)
#                               s.append(duration)
#                                print(s)
                                error = 'false'
                                for e in k['tags']:
                                    if e['key']=='error' and e['value']=='true':
                                        error = 'true'
                                duartionlist.append([traceId,svcName1,spanId1,svcName2,spanId2,duration,error])
#                                print(duartionlist)

    duartionlist = [x for x in duartionlist if x]
    return duartionlist    #返回值为【traceid, 该traceid对应的span】

def createtraceList(arr):
    n=0
    tracelist= []

    for i in arr:
        for j in i:
            if j['process']['serviceName'] == 'ts-order-service.default':          #建立traceID数组
                tracelist.append(j['duration'])

    tracelist = [str(x) for x in tracelist if x]
    return tracelist    #返回值为【traceid, 该traceid对应的span】