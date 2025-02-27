def solution(brown, yellow):
    
    width = brown // 2
    height = brown // 2
    
    for x in range(3, width):
        for y in range(3,height):
            if ((2 * x) + (2 * y) - 4 == brown) and ((x - 2) * (y - 2) == yellow) and (x >= y):
                return [x, y]
