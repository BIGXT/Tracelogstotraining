# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import copy

import creattraceList
import duration
import file
import datapre
import time

def printarray(arr):
    j = 0
    for i in arr:
        j = j + 1
        print(j)
        print(i)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    time_start = time.time()

    fnum = 10  # 样本故障数量，即f文件数
    ftype = 1  # 数据类型，0训练集，1测试集,2原始数据

    starttime = 1610275905145119  # 最早的trace时间戳 f10:1610275905145119 1610276518529901 f9:1610273858962973  f8:1610269382179702  f7；1610267887435795 f6:1610265600201338 1610265668938415 f5:1610258292130405  f4:1610246355193952 f3:1610239874090341 f2:1610182441071756 1610185462247515 f1:1610251577242887 t:1609886090644744 1610174198993375
    endtime = 1610277483004658   # 最晚的trace时间戳 f10:1610277483004658 f9:1610275085369240  f8:1610270576991463  f7:1610269079828434  f6:1610266867042277 1610266867042277 f5:1610259509135717  f4:1610247613395105 f3:1610241088782813 f2；1610183045278038 1610186045239267 f1:1610252758241564 t:16098860906447440 1610175261006404
    fstarttime = 1610276884328940 # 故障注入时间 f10:1610276884328940  f9:1610274481338380  f8:1610269980732856  f7:1610268481696586  f6:1610266260909189 1610266260909189  f5:1610258880210944  f4:1610246940003826 f3:1610240460084686 f2:1610185462247515 f1:1610252176395048
    fendtime = 1610277177881119   # 故障消失时间 f10:1610277177881119  f9:1610274784846119  f8:1610270284701933  f7:1610268784779536  f6:1610266569723126  1610266559999605 f5:1610259209513313  f4:1610247239978701 f3:1610240769817978  f2:1610185749852030 f1:1610252459855042

    if ftype == 2:
        print((fstarttime-starttime)/(endtime-fendtime))
        # a = file.readjsonfile('test.json')
        # a = file.readjsonfile('data.json')
        # a = file.readjsonfile('ordata.json')
        a = file.readjsonfile('f10.json')

        a = creattraceList.createtraceList(a)
        a = creattraceList.getSameTraceidSpan(a)

        # a = creattraceList.dataScreening(a, 1, starttime, endtime)
        # file.writejsonfile('training.json', a)

        a1 = copy.deepcopy(a)
        a2 = copy.deepcopy(a)
        a3 = copy.deepcopy(a)
        a1 = creattraceList.dataScreening(a1, 2, starttime, 1610276518529901)
        a2 = creattraceList.dataScreening(a2, 2, fstarttime, fendtime)
        a3 = creattraceList.dataScreening(a3, 2, fendtime, endtime)
        file.writejsonfile('fault10-1.json', a1)
        file.writejsonfile('fault10-2.json', a2)
        file.writejsonfile('fault10-3.json', a3)

        exit(0)

    for i in range(1, fnum + 1):
        a = []
        b = []
        d = []
        s = []
        sq = []
        aD = []
        ha = []
        Nstr = []
        Fstr = []
        j = 1
        if ftype == 0:
            a = file.readjsonfile('training.json')
            a = creattraceList.createtraceList(a)
            a = creattraceList.getSameTraceidSpan(a)
        elif ftype == 1:
            a1 = file.readjsonfile('fault' + str(i) + '-1.json')
            a1 = creattraceList.createtraceList(a1)
            a1 = creattraceList.getSameTraceidSpan(a1)

            a2 = file.readjsonfile('fault' + str(i) + '-2.json')
            a2 = creattraceList.createtraceList(a2)
            a2 = creattraceList.getSameTraceidSpan(a2)

            a3 = file.readjsonfile('fault' + str(i) + '-3.json')
            a3 = creattraceList.createtraceList(a3)
            a3 = creattraceList.getSameTraceidSpan(a3)

        if ftype == 0:
            # a = creattraceList.dataScreening(a, 1, starttime, endtime)
            file.writetxtfile('atraining.txt', a)
            d = duration.getDurationList(a)
        elif ftype == 1:
            # a = creattraceList.dataScreening(a, 0, starttime, endtime)
            file.writetxtfile('a' + str(i) + '-1fault.txt', a1)
            file.writetxtfile('a' + str(i) + '-2fault.txt', a2)
            file.writetxtfile('a' + str(i) + '-3fault.txt', a3)


        # print(a)
        #    Str=faultString.createFaultString(a)
        # for i in a:
        #    print(i['_source']['traceID'])
        # printarray(createDAG(a))
        #   file.writejsonfile("result.txt",a)
        #  file.writejsonfile("str.txt", Str)
        if ftype == 0:
            file.writetxtfile('rtraining.txt', d)
            s = datapre.getAllService(a)
            ha = datapre.hashStr(s)
            Nstr = datapre.getNorHashStrArr(d)
            Fstr = datapre.getFaultHashStrArr(d)
            file.writetxtfile('allService.txt', s)
            file.writetxtfile('norstr.txt', Nstr)
            file.writetxtfile('fault.txt', Fstr)
            aD = datapre.avgDuration(d, s)
            file.writecsvfile('avgDuration.csv', aD)
            sq = datapre.training1(d, s, aD, Nstr, Fstr, [], 0)
            file.writecsvfile('training.csv', sq)
            break
        elif ftype == 1:
            j = 0

            for j in range(1, 4):

                if j == 1:
                    a = copy.deepcopy(a1)
                elif j == 2:
                    a = copy.deepcopy(a2)
                elif j == 3:
                    a = copy.deepcopy(a3)
                d = duration.getDurationList(a)
                file.writetxtfile('r' + str(i) + '-' + str(j) + 'fault.txt', d)
                s = file.readtxtfile('allService.txt')
                FaultServiceList = [[], 'ts-station-service.default', 'ts-cancel-service.default',
                                    'ts-travel2-service.default',
                                    'ts-admin-user-service.default', 'ts-admin-route-service.default','ts-order-service.default',s,s,'ts-notification-service.default','ts-config-service.default']

                ha = datapre.hashStr(s)
                for ns in (file.readtxtfile('norstr.txt')):
                    Nstr.append(ns[0])
                for fs in (file.readtxtfile('fault.txt')):
                    Fstr.append(fs[0])
                aD = file.readcsvfile('avgDuration.csv')
                if j == 1:
                    sq = datapre.training1(d, s, aD, Nstr, Fstr, FaultServiceList[0], 0)
                elif j == 2:
                    sq = datapre.training1(d, s, aD, Nstr, Fstr, FaultServiceList[i], i)
                elif j == 3:
                    sq = datapre.training1(d, s, aD, Nstr, Fstr, FaultServiceList[0], 0)
                # sq = datapre.training1(d, s, aD, Nstr, Fstr, FaultServiceList[i], i)
                file.writecsvfile('f' + str(i) + '-' + str(j) + 'training.csv', sq)

    time_end = time.time()
    print('totally cost', time_end - time_start)
#   print(faultString.findTheNearestFault("test.json","str.txt"))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
