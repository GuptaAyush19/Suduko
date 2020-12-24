# Project: Suduko Solver
# Author : Ayush Gupta
# Date created : 24-12-2020    

def empty(puzzle):
    # arguement: 2d list
    # returns: list (only two values of the empty square)
    for y in range(9):
        for x in range(9):
            if puzzle[y][x] == 0 :
                return y,x
    
    return None, None

def valid_value(puzzle, y, x, value):
    # checks whether the value is valid for that coordinate
    
    # [1] : check the x-axis
    for i in range(9):
        if puzzle[y][i] == value:
            return False
        
    # [2] : check the y-axis
    for j in range(9):
        if puzzle[j][x] == value:
            return False
        
    # [3] : check the local square
    x0 = (x//3)*3
    y0 = (y//3)*3
    for r in range(y0, y0+3):
        for c in range(x0, x0+3):
            if puzzle[r][c] == value:
                return False
            
    return True

def valid_value2(puzzle, y, x, value):
    # checks whether the value is valid for that coordinate
    
    # [1] : check the x-axis
    for i in range(9):
        if i!=x:
            if puzzle[y][i] == value:
                return False
        
    # [2] : check the y-axis
    for j in range(9):
        if j!=y:
            if puzzle[j][x] == value:
                return False
        
    # [3] : check the local square
    x0 = (x//3)*3
    y0 = (y//3)*3
    for r in range(y0, y0+3):
        for c in range(x0, x0+3):
            if x!=c and y!=r:
                if puzzle[r][c] == value:
                    return False
            
    return True

def solve(puzzle):
    y,x=empty(puzzle)
    # puzzle is completed if there aren't any boxes left
    if y is None:
        return True
    for guess in range(1,10):
        if valid_value(puzzle, y, x, guess):
            puzzle[y][x] = guess
            if solve(puzzle):
                return True
        puzzle[y][x] = 0
    return False

def solved(puzzle):
    answer=""
    for i in range(9):
        for j in range(9):
            if j==3 or j==6:
                answer += "  |"
            answer += "  "+str(puzzle[i][j])
        answer += "\n"
        if i==2 or i==5:
            answer += " ---------------------------------\n"
    return answer

def print_board(puzzle):
    print(solved(puzzle),end="")
            
# open the text file and read the grid
grid = [[]for i in range(9)]
file = open("suduko.txt", "r")
fileInfo = file.read()
file.close()

def readFileInfo():
    ngrid = grid.copy()
    j = 0
    for num in fileInfo:
        if len(ngrid[j])==9:
            j+=1
        if num.isdigit():
            ngrid[j].append(int(num))
        elif num == "-":
            ngrid[j].append(int(0)) 
    return ngrid  
            
grid = readFileInfo() 
        
if __name__ == "__main__":
    if solve(grid):
        print("\nSolution:\n")
        print_board(grid)
        file = open("solution.txt","w")
        file.write(str(solved(grid)))
        file.close()
        print("\nCopied the solution to <solution.txt>")
        
        # testing the solution
        for y in range(9):
            for x in range(9):
                if not valid_value2(grid, y, x, grid[y][x]):
                    print("\nTHERE IS A PROBLEM, please input a valid grid\n")
                    break
    else:
        print("There is a problem")