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

if __name__ == '__main__':
    grid = list()
    count_path(grid, 8, 8)
