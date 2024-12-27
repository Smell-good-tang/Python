'''def fib_recur(n):
    if n <= 1: #判定n项项数是否能参与计算
        return n
    else:
        return fib_recur(n - 1) + fib_recur(n - 2) #斐波那契数列通用求第n项值公式

X = int(input('请输入正整数：\n')) #输入X
print('前',X,'项分别为：') #输出前X项前的提示
for i in range(X+1): #循环语句依顺序输出第i项
    print(fib_recur(i), end=' ') #依顺序输出
def FindGreatestSumOfSubArray(pData,nLength,nGreatestSum,start,end)
'''

start1,end1=0,0    #定义“当前的”Start，End变量，并赋值
def FindGreatestSumOfSubArray(pdata, nlength, ngreatestsum, start, end):
    #如果所输入数值无效，则不参与运算，返回false
    if pdata == '' or nlength == 0:
        False
    ncursum, ngreatestsum = 0, 0    #定义“当前的”数组和，并赋值
    curstart, curend = 0, 0
    global start1,end1           #使用全局变量start1，end1
    for i in range(nlength):
        ncursum = int(pdata[i]) + ncursum
        curend = i
        #如果当前的数组和小于0，则舍弃
        if ncursum < 0:
            ncursum = 0
            curstart = curend = i + 1
        #如果找到了更大的子数组和，那就把它作为当前最大的数组和
        if ncursum > ngreatestsum:
            ngreatestsum = ncursum
            start = curstart
            end = curend
    #如果所有的列值都小于0，那么在所给数组中找最大的列值
    if ngreatestsum == 0:
        ngreatestsum = pdata[0]
        start, end = 0, 0
        for i in range(1, nlength - 1):
            if pdata[i] > ngreatestsum:
                ngreatestsum = pdata[i]
                start = end = i
    start1,end1=start,end
    return ngreatestsum
    True

n = int(input('请输入数列的长度:'))
print('请依次输入数列的列值:',end="")
arr = list(range(n))    #给长度为n的数组arr赋值
arr = list(input().split())    #不换行给数组arr赋值
igreatestsum= 0
start,end=0,0
print('所求最大子数组和为:', FindGreatestSumOfSubArray(arr, n, igreatestsum, start, end), '\t对应数组为:',end="")
for iii in range(start1,end1+1):   #依次输出最大子数组的各项列值
    print(arr[iii],' ',end="")
