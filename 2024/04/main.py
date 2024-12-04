import os
dirname = os.path.dirname(__file__)

with open(f"{dirname}/input.txt") as f:
    matrix = f.read().splitlines()
    width = len(matrix[0])
    height = len(matrix)

def checkHorizontal(x: int, y: int) -> bool:
    return matrix[y][x:].startswith("XMAS") or matrix[y][x:].startswith("SAMX")

def checkVertical(x: int, y: int) -> bool:
    if y + 3 >= height: return False

    if matrix[y][x] == 'X':
        if matrix[y + 1][x] != 'M': return False
        if matrix[y + 2][x] != 'A': return False
        if matrix[y + 3][x] != 'S': return False
        return True

    elif matrix[y][x] == 'S':
        if matrix[y + 1][x] != 'A': return False
        if matrix[y + 2][x] != 'M': return False
        if matrix[y + 3][x] != 'X': return False
        return True
    else:
        return False

def checkDiagonal1(x: int, y: int) -> bool:
    if x + 3 >= width or y + 3 >= height: return False

    if matrix[y][x] == 'X':
        if matrix[y + 1][x + 1] != 'M': return False
        if matrix[y + 2][x + 2] != 'A': return False
        if matrix[y + 3][x + 3] != 'S': return False
        return True

    elif matrix[y][x] == 'S':
        if matrix[y + 1][x + 1] != 'A': return False
        if matrix[y + 2][x + 2] != 'M': return False
        if matrix[y + 3][x + 3] != 'X': return False
        return True
    else:
        return False

def checkDiagonal2(x: int, y: int) -> bool:
    if x + 3 >= width or y + 3 >= height: return False

    if matrix[y + 3][x] == 'X':
        if matrix[y + 2][x + 1] != 'M': return False
        if matrix[y + 1][x + 2] != 'A': return False
        if matrix[y][x + 3] != 'S': return False
        return True

    elif matrix[y + 3][x] == 'S':
        if matrix[y + 2][x + 1] != 'A': return False
        if matrix[y + 1][x + 2] != 'M': return False
        if matrix[y][x + 3] != 'X': return False
        return True
    else:
        return False



def part1():
    count = 0

    y = 0
    while y < height:
        x = 0
        while x < width:
            if checkHorizontal(x, y): count += 1
            if checkVertical(x, y): count += 1
            if checkDiagonal1(x, y): count += 1
            if checkDiagonal2(x, y): count += 1
            x += 1 
        y += 1

    print(f"part 1: {count}")

def checkCross(x: int, y: int) -> bool:
    if x + 1 >= width - 1 and y + 1 >= height - 1:
        return False
    
    if matrix[y][x] != 'A':
        return False
    
    mas1 = matrix[y - 1][x - 1] == 'M' and matrix[y + 1][x + 1] == 'S'
    mas2 = matrix[y + 1][x - 1] == 'M' and matrix[y - 1][x + 1] == 'S'

    sam1 = matrix[y - 1][x - 1] == 'S' and matrix[y + 1][x + 1] == 'M'
    sam2 = matrix[y + 1][x - 1] == 'S' and matrix[y - 1][x + 1] == 'M'

    return (mas1 or sam1) and (mas2 or sam2)

def part2():
    count = 0

    y = 1
    while y < height - 1:
        x = 1
        while x < width - 1:
            if checkCross(x, y): count += 1
            x += 1 
        y += 1

    print(f"part 2: {count}")

if __name__ == "__main__":
    part1()
    part2()
