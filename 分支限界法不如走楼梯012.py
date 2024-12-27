from queue import Queue


def bfs(n, a, b, k):
    f = [False] * (n + 1)  # 标记楼层是否访问过
    q = Queue()  # 定义队列
    p = [a, 0]
    q.put(p)  # 进入队列
    while (not q.empty()):  # 队列非空
        p = q.get()
        if (f[p[0]]):  # 判断楼层是否被访问过
            continue
        f[p[0]] = True  # 标记楼层访问过
        if (p[0] == b):  # 判断是否到达目标楼层
            return p[1]  # 子函数结束
        if (p[0] - k[p[0] - 1] > 0):  # 向下按，若不会下到负楼层，那么执行下面的一条代码段
            t = [p[0] - k[p[0] - 1], p[1] + 1]  # 当前按按钮之后，到了第几层，按钮次数加1
            q.put(t)  # 当前按按钮的次数参与接下来的q队列while循环
        if (p[0] + k[p[0] - 1] <= n):  # 向上按，若不会上到天台，或上天，那么执行下面的一条代码段
            t = [p[0] + k[p[0] - 1], p[1] + 1]  # 当前按按钮之后，到了第几层，按钮次数加1
            q.put(t)  # 当前按按钮的次数参与接下来的q队列while循环
    return -1


n = int(input("请输入楼梯总层数："))
a = int(input("请输入开始层："))
b = int(input("请输入结束层："))
print('请依次为每层能上下的层数赋值：', end='')
k = list(range(n))
k = list(input().split())  # 为每层能上下的层数赋值
k = list(map(int, k))  # 将数组类型转化为整型
result = bfs(n, a, b, k)  # 执行子函数
if result == -1:
    print('指定条件无法到达')
    exit(-1)
print(f"最少的按键次数为{result}次")
