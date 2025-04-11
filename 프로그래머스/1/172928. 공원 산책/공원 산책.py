def solution(park, routes):
    
    dimX = len(park[0])
    dimY = len(park)
    b = [["X"] * (dimX + 2) for _ in range(dimY + 2)]
    y, x = 0, 0
    
    for py in range(dimY):
        for px in range(dimX):
            p = park[py][px]
            if p == "S":
                y, x = py + 1, px + 1

            b[py + 1][px + 1] = p
            
    for inst in routes:
        t, d = inst.split()
        
        if t == "E":
            dy, dx = 0, 1
        elif t == "W":
            dy, dx = 0, -1
        elif t == "S":
            dy, dx = 1, 0
        else:
            dy, dx = -1, 0
            
        ty, tx = y, x
        valid = True
        
        for _ in range(int(d)):
            ty, tx = ty + dy, tx + dx
            if b[ty][tx] == "X":
                valid = False
                break
        if valid:
            y, x = ty, tx
            
            
    return [y - 1, x - 1]