def _sum(arr):
    return sum(map(int, arr))


def makequre(nums):
    # 从大到小排序
    nums = sorted(nums, reverse=True)
    return nums


def equvalient(a, b):
    if a == b:
        return True
    else:
        return False


def helper(a, arrhc, c, arrhe) -> object:
    if a >= len(arrhc):
        return [equvalient(arrhe[i], c) for i in range(4)]
    for j in range(4):
        # 每条边上存储的火柴不超过数组总和的1/4
        if arrhe[j] + arrhc[a] > c:
            continue
        arrhe[j] = arrhc[a] + arrhe[j]
        if helper(a + 1, arrhc, c, arrhe):
            return True
        arrhe[j] = arrhe[j] - arrhc[a]
    return False


n = int(input('请输入参与计算的火柴棒数量:'))
if n < 4:
    print("所使用的火柴棒数量不够")
    exit(-1)
print('为每个火柴棒设计长度:', end="")
nums = list(range(n))  # 给长度为n的数组nums赋值
nums = list(map(int, input().split()))  # 不换行给数组nums赋值，！！！！！！
summary = _sum(nums)
if summary % 4 != 0:
    print("所使用的火柴棒总长度不满足要求")
    exit(-1)
makequre(nums)
bucket = [0] * 4
bucket = list(map(int, bucket))  # !!!!!!
if helper(0, nums, summary // 4, bucket) == 0:
    print("组不成")
    exit(-1)
else:
    print('能')
    exit(-1)
