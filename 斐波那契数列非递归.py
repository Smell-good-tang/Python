def fib_loop(n):
    a, b = 0, 1 #定义变量并赋值
    if n == 0:  # 第0项值为0
        a = 0
    for i in range(n + 1):
        a, b = b, a + b
    return a

X = int(input("要求斐波那契数列第几项：")) #输入要求斐波那契数列项数X
print('第',X,'项是：',end="") #输出第X项前的提示
print(fib_loop(X-1)) #输出结果