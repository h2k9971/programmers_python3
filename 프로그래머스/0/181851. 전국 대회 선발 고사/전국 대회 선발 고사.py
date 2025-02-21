def solution(rank, attendance):
    
    dict = {}
    
    for i in range(len(rank)):
        dict[i] = [rank[i], attendance[i]]
        
    arr = []
    
    for item in dict.items():
        if item[1][1] == True:
            arr.append(item)
        
    arr = sorted(arr, key = lambda x : x[1])
    answer = 10000 * arr[0][0] + 100 * arr[1][0] + arr[2][0]
    
    return answer