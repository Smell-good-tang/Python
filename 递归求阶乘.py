def num(n):
    if n == 0:
        return 1
    else:
        return n * num(n - 1)
n=int(input("请输入要求阶乘的整数："));
for i in range(1,n+1):
    print(i,"的阶乘为：",num(i));
