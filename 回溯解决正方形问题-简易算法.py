def makequre(nums):
    nums_sum = sum(nums)
    # 数组长度小于4或者数组总和对4取余不为0
    if len(nums) < 4:
        return 'error1'
    elif nums_sum % 4 != 0:
        return 'error2'
    # 从大到小排序
    nums = sorted(nums, reverse=True)
    # 储存火柴
    nums2 = [[] for i in range(4)]
    return helper(0, nums, nums_sum // 4, nums2)

def helper(i, nums, result, nums2):
    if i >= len(nums):
        return [[result] for i in range(4)]
    for j in range(4):
        # 每条边上存储的火柴不超过数组总和的1/4
        if sum(nums2[j]) + nums[i] > result:
            continue
        nums2[j].append(nums[i])
        if helper(i + 1, nums, result, nums2):
            return True
        nums2[j].pop()
        return False

nums = list(map(int, input().split()))
if makequre(nums) == True:
    print("能组成正方形")
elif makequre(nums) == 'error1':
    print("所使用的火柴棒数量不够")
elif makequre(nums) == 'error2':
    print("所使用的火柴棒总长度不满足要求")
else:
    print("组不成正方形")
