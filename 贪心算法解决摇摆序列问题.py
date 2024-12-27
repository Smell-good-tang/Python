def get_max_length(a):
    l = len(a)
    if l < 2:  # 如果原数组长度小于2，那么所求数组长度就是2
        return -1
    else:
        symbol = 0  # 相邻的差值正负判定
        max = 1  # 所求数组长度
        for i in range(1, l):  #
            if a[i] - a[i - 1] > 0 and symbol <= 0:  # 如果差值大于0并且前一个差值小于0或等于0
                max += 1  #
                symbol = symbol == 0  # symbol如果等于0/false，则给symbol赋值true/1，否则赋值false/true
            elif a[i] - a[i - 1] < 0 and symbol >= 0:  # 如果差值小于0并且前一个差值大于0或等于0
                max += 1  #
                symbol = -1  # symbol设定为负（差值为负），参与下一个循环判定
        return max


n = int(input('请输入数组长度：'))
if n < 2:
    print('所输入数组不满足解题要求：因为数组长度必须大于1。')
    exit(-1)
a = list(range(n))
a = list(map(int, a))
print('请为数组依次赋值：', end='')
a = list(map(int, input().split(' ')))
result = get_max_length(a)
if result == 1:
    print('所输入数组元素值全都相同，所以数组不满足解题要求。')
    exit(-1)
print('所求的数组长度为：', result)
