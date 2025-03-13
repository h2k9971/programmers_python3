def solution(wallpaper):
    location_row = []
    location_column = []
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            
            if wallpaper[i][j] == '#':
                location_row.append(i)
                location_column.append(j)
    
    # print(location_row, location_column)
    lux = min(location_row)
    luy = min(location_column)
    rdx = max(location_row) + 1
    rdy = max(location_column) + 1
                
    return [lux, luy, rdx, rdy]