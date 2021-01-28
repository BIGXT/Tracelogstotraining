import file
import hashlib
import Levenshtein as PL
from array import array


def getAllService(list):
    s = []
    service = []
    for l in list:
        for m in l:
            if m['process']['serviceName'] not in s:
                s.append(m['process']['serviceName'])

    for l in s:
        service.append([l])
    return service


def avgDuration(list, service):
    a = []
    for s1 in service:
        for s2 in service:
            a.append([s1[0], s2[0], 0, 0, 0])

    for l in list:
        for m in a:
            if l[1] == m[0] and l[3] == m[1]:
                m[2] = (m[2] * m[3] + l[5]) / (m[3] + 1)
                m[3] = m[3] + 1
                # break

    for l in list:
        for m in a:
            if l[1] == m[0] and l[3] == m[1]:
                if m[3] >= 2:
                    m[4] = pow((l[5] - m[2]) * (l[5] - m[2]) / (m[3] - 1), 0.5)
                else:
                    m[4] = 0
                break
    return a

    # for s1 in service:
    #    for s2 in service:
    #        for l in list:
    #            if l[1]==s1 and l[3] == s2:
    #
    #                a


def training1(list, service, duration, N, F, FaultService, FaultNo):
    traceid = []
    sq = []
    e=[]
    num = len(service)
    for l in list:
        if l[0] not in traceid:
            traceid.append(l[0])

    for t in traceid:
        x = [t]
        error = 0
        terror = 0
        for i in range(num):
            for j in range(num):
                x.append(0)
                e.append(0)

        for l in list:

            if l[0] == t:
                hang = 0
                lie = 0

                for s1 in service:
                    hang = hang + 1
                    lie = 0
                    for s2 in service:
                        lie = lie + 1
                        if s1[0] == l[1] and s2[0] == l[3]:
                            for d in duration:
                                if s1[0] == d[0] and s2[0] == d[1]:
                                    if d[4] == 0.0 or d[4] == '0':
                                        x[hang * num + lie] = 1
                                    else:
                                        x[hang * num + lie - num] = abs(int(l[5]) - float(d[2])) / float(d[4])
                                    if s2[0] in FaultService or s1[0] in FaultService or l[6] == 'true':
                                        terror = 1

                                    e[hang * num + lie] = e[hang * num + lie]+1

                if l[6] == 'true':
                    error = 1

        h = getHashStrArr(list, t)  # 计算与错误/正常字符串的最小编辑距离
        x.append(getMinEditDis(N, h))
        x.append(getMinEditDis(F, h))
        x.append(error)  # 是否含有错误码

        for es in e:
            x.append(es)

        # x.append(n)  # 实际是否错误/正确
        x.append(terror)  # 实际是否错误/正确
        if terror == 1:
            for s in service:  # 为故障服务打上标记
                if s[0] in FaultService:
                    x.append(1)
                else:
                    x.append(0)
            for no in range(1, 11):  # 标记故障编号
                if no == FaultNo:
                    x.append(1)
                else:
                    x.append(0)
        else:
            for s in service:  # 为故障服务打上标记
                x.append(0)
            for no in range(1, 11):  # 标记故障编号
                x.append(0)
        sq.append(x)
    return sq


def hashStr(service):
    h = []
    for s in service:
        m = hashlib.md5(s[0].encode("utf8"))
        mi = m.hexdigest()
        h.append([s[0], mi])
    return h


def getMinEditDis(list, str):
    min = len(str)
    for l in list:
        if PL.distance(l, str) < min:
            min = PL.distance(l, str)
    return min


# def writeServiceListToFile(list):


def getHashStrArr(list, traceid):
    Str = ''
    for l in list:
        if l[0] == traceid:
            m1 = hashlib.md5(l[1].encode("utf8"))
            mi1 = m1.hexdigest()
            m2 = hashlib.md5(l[3].encode("utf8"))
            mi2 = m2.hexdigest()
            Str = Str + mi1 + mi2
    # print(Arr)
    return Str


def getNorHashStrArr(list):
    traceid = []
    for l in list:
        if l[0] not in traceid:
            traceid.append(l[0])

    Arr = []
    for t in traceid:
        error = 0
        Str = ''
        for l in list:
            if l[0] == t:
                if l[6] == 'true':
                    error = 1
                    break
                m1 = hashlib.md5(l[1].encode("utf8"))
                mi1 = m1.hexdigest()
                m2 = hashlib.md5(l[3].encode("utf8"))
                mi2 = m2.hexdigest()
                Str = Str + mi1 + mi2
        if Str not in Arr and Str != '' and error == 0:
            Arr.append(Str)
    # print(Arr)
    return Arr


def getFaultHashStrArr(list):
    traceid = []
    for l in list:
        if l[0] not in traceid:
            traceid.append(l[0])

    Arr = []
    for t in traceid:
        error = 0
        Str = ''
        for l in list:
            if l[0] == t:
                if l[6] == 'true':
                    error = 1
                m1 = hashlib.md5(l[1].encode("utf8"))
                mi1 = m1.hexdigest()
                m2 = hashlib.md5(l[3].encode("utf8"))
                mi2 = m2.hexdigest()
                Str = Str + mi1 + mi2
        if Str not in Arr and Str != '' and error == 1:
            Arr.append(Str)
    return Arr
