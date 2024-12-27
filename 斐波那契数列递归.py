def fib_recur(n):
    if n <= 1: #判定n项项数是否能参与计算
        return n
    else:
        return fib_recur(n - 1) + fib_recur(n - 2) #递归法-斐波那契数列通用求第n项值公式

X = int(input('要求斐波那契数列第几项：')) #输入斐波那契数列第X项
print('第',X,'项为：',end="") #输出第X项前的提示
print(fib_recur(X), end=' ') #输出第X项
