# 动态规划

'''
leecode 152. 乘积最大子数组
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），
并返回该子数组所对应的乘积。

示例 1:
输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。

示例 2:
输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
'''
def maxProduct_1(nums):
    if nums is None: return 0

    dpmax = [0 for _ in range(len(nums))]
    dpmin = [0 for _ in range(len(nums))]

    dpmax[0], dpmin[0], res = nums[0], nums[0], nums[0]

    print('dpmax[0]=%s' %dpmax[0])
    print('dpmin[0]=%s' %dpmin[0])

    for i in range(1, len(nums)):
        dpmax[i] = max(dpmax[i-1] * nums[i], dpmin[i-1] * nums[i], nums[i])
        dpmin[i] = min(dpmin[i-1] * nums[i], dpmax[i-1] * nums[i], nums[i])

        res = max(res, dpmax[i])
        
        print(res, '\n')

    print(dpmax)        
    print(dpmin)
    
    return res

def maxProduct(nums):
    if nums is None: return 0

    dp = [[0 for _ in range(2)] for _ in range(2)]

    dp[0][1], dp[0][0], res = nums[0], nums[0], nums[0]

    print('dp[0][0]=%s, dp[0][1]=%s' %(dp[0][0], dp[0][1]))
    print('dp[1][0]=%s, dp[1][1]=%s' %(dp[1][0], dp[1][1]))

    for i in range(1, len(nums)):
        x, y = i%2, (i-1) %2       
        dp[x][0] = max(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
        dp[x][1] = min(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])

        print('第 %s 步，x=%s y=%s num[i]=%s' %(i, x, y, nums[i]))
        print('dp[x][0]=%s, dp[x][1]=%s' %(dp[x][0], dp[x][1]))
        print('dp[y][0]=%s, dp[y][1]=%s' %(dp[y][0], dp[y][1]))

        res = max(res, dp[x][0])

    return res


if __name__ == '__main__':
    nums = [1, 5, -1, 2, 3]
    print(maxProduct(nums))
