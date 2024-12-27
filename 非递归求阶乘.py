a = int(input('please input a integer:'))
num = 1
if a < 0:
    print('负数没有阶乘！')
elif a == 0:
    print('0的阶乘为1！')
else :
    for i in range(1,a + 1):
        num *= i
        print(i,"的阶乘为：",num);
