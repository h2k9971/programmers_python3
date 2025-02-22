def solution(arr):
    
    row = len(arr)
    column = len(arr[0]) 
    count = abs(row - column)

    if row > column:
        for i in range(row): 
            arr[i].extend([0] * count) 
    
    elif row < column:
        for i in range(count):
            arr.append([0] * column)

    return arr