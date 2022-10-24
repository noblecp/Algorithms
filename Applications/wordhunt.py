from colorama import Fore, Style

from english_words import english_words_set

def pretty(matrix):
    for row in matrix:
        print(Fore.GREEN + " ".join(row))

def prettySelect(matrix, x, y):
    '''
    Function visually isolates a given cell (x, y) in given matrix
    '''
    print("---")
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if x==c and y==r:
                if c == dims-1:
                    print(Fore.RED + matrix[r][c])
                else:
                    print(Fore.RED + matrix[r][c], end=" ")
            else:
                if c == dims-1:
                    print(Style.RESET_ALL + matrix[r][c])
                else:
                    print(Style.RESET_ALL + matrix[r][c], end=" ")

dims = int(input("NxN: "))
matrix = [[None for r in range(dims)] for c in range(dims)]
minLength = int(input("Minimum length word: "))
board = input("Enter the board: ")

rowsInput = [board[index : index + dims] for index in range(0, len(board), dims)]

for r in range(dims):
    matrix[r] = list(rowsInput[r])

result = []
visited = [[False for r in range(dims)] for c in range(dims)]
seen = set()

def dfs(row, col, matrix, path):
    visited[row][col] = True
    path += matrix[row][col]

    # add path to result if it falls within valid constraints and is an englsh word
    if len(path)>=minLength and path not in seen and path in english_words_set:
        result.append(path)
        seen.add(path)
    
    # easily handle neighbors in all directions
    dirs = [[1, 0],[-1, 0],[-1, -1],[1, 1],[-1, 1],[1,-1],[0, 1],[0, -1]] # [x, y]
    
    # perform dfs on neighbors in case that it is a valid direction
    for dx, dy in dirs:
        r, c = row + dx, col + dy
        if r in range(dims) and c in range(dims) and visited[r][c]==False:
            dfs(r, c, matrix, path) # recursive dfs call
    
    # reset the visited status for backtracking
    visited[row][col] = False

# run dfs on the character matrix
for r in range(dims):
    for c in range(dims):
        dfs(r, c, matrix, "")

# print matrix
# pretty(matrix)

# sort result array by non-decreasing length
result.sort(key=lambda x: len(x))

# print result words found in the character graph
for res in result:
    print(Fore.YELLOW + res)