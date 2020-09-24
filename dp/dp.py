# 动态规划

# 路径问题，n*m格，1为石头，不可通行
# 从n-1,m-1到0，0，每次只能走一步，只能向下或向右，一共有多少种走法
def init_maze(rows, cols):
    grid = [[0 for col in range(cols)] for row in range(rows)]
    grid[1][2] = 1
    grid[1][6] = 1
    grid[2][1] = 1
    grid[2][3] = 1
    grid[2][4] = 1
    grid[3][5] = 1
    grid[4][2] = 1
    grid[4][5] = 1
    grid[4][7] = 1
    grid[5][3] = 1
    grid[6][1] = 1
    grid[6][5] = 1

    for row in range(rows-1,-1,-1):
        print(grid[row][::-1])
         
    return grid

def count_path(grid, rows, cols):
    grid = init_maze(rows, cols)

    opt = [[0 for col in range(cols)] for row in range(rows)]
 
    for i in range(rows):
        for j in range(cols):
            if i==0 or j==0:
                opt[i][j] = 1
            elif grid[i][j] == 1:
                opt[i][j] = 0
            else:
                opt[i][j] = opt[i-1][j] + opt[i][j-1]
    
    path_num = opt[rows-1][cols-1]
    
    print(path_num)

    return path_num

'''
递推，从结果往前推导
第n层的总走法等于(n-1)层的总走法+(n-2)层的总走法
n-1到n，只需走一步，
n-2到n，只需走两步，如果走一步，那就变成了n-1的一种走法
n-1、n-2这样走，相当于各自原来的总走法增加了一步/两步，但走法数量不变，所以二者相加就是n的总走法
'''
def climbStairs(n):
    f = [0 for i in range(n+1)]
    f[1] = 1
    f[2] = 2

    for i in range(1,n+1):
        if i<=2:
            f[i] = i
        else:
            f[i] = f[i-1] + f[i-2]

    print(f[n])

'''
leecode 70. 爬楼梯
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
'''
def climbStairs1(n):    # 只使用三个变量完成递推
    first_step=1
    second_step=2

    final_step = 1

    for i in range(1,n+1):
        if i<=2:
            final_step = i
        else:
            final_step = first_step + second_step
            first_step = second_step
            second_step = final_step            

    print(final_step)


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

'''
leecode 62. 不同路径
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？


示例 1:
输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
示例 2:

输入: m = 7, n = 3
输出: 28
'''
def uniquePaths(m: int, n: int) -> int:
    opt = [[0 for cols in range(m)] for row in range(n)]
    print(opt)
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if i == n-1 or j == m-1:
                opt[i][j] = 1
            else:
                opt[i][j] = opt[i][j+1] + opt[i+1][j]
        print(opt)
    return opt[0][0]

if __name__ == '__main__':
    # grid = list()
    # count_path(grid, 8, 8)
    # print(fib(6))

    # climbStairs1(6)

    # uniquePaths(7,3)

    # nums = [1, 5, -1, 2, 3]
    nums = [-2]
    print(maxProduct(nums))
