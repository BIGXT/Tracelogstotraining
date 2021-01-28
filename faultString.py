import hashlib
import numpy as np

import creattraceList
import file


def createFaultString(list):
    flist=[]

    for i in list:
        str = []
        for j in i:
            m = hashlib.md5()
            b = j['process']['serviceName'].encode(encoding='utf-8')
            m.update(b)
            n=m.copy()
            str.append(n.hexdigest())
        flist.append(str)
    return flist

def findTheNearestFault(filename, strfilename):
    unknownfault=[]
    unknownfaultlist=[]
    unknownfaultstr=''
    distance=0
    l=0

    unknownfault=file.readjsonfile(filename)
    unknownfault=creattraceList.createtraceList(unknownfault)
    unknownfault=creattraceList.getSameTraceidSpan(unknownfault)
    unknownfaultlist=createFaultString(unknownfault)[0]
    unknownfaultstr=unknownfaultstr.join(unknownfaultlist)

    f = open(strfilename, "r")  # 返回一个文件对象
    line = f.readline()  # 调用文件的 readline()方法
    l=l+1

    while line:
        distance=distance+ld(line,unknownfaultstr)
        line = f.readline()
        l = l + 1
    f.close()
    return distance/l

def ld(str1, str2):
    dp=np.zeros((len(str1)+1,len(str2)+1))
    m=len(str1)
    n=len(str2)
    for k in range(1,m+1):
        dp[k][0]=k
    for k in range(1,n+1):
        dp[0][k]=k
    for k in range(1,m+1):
        for j in range(1,n+1):
            dp[k][j]=min(dp[k-1][j],dp[k][j-1])+1 #这里表示上边和下边的数值最小数值
            if str1[k-1]==str2[j-1]:
                dp[k][j]=min(dp[k][j],dp[k-1][j-1])
            else:
                dp[k][j]=min(dp[k][j],dp[k-1][j-1]+1)
    return dp[m-1][n-1]



