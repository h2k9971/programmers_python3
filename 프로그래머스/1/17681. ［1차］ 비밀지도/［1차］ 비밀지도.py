def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        row = bin(arr1[i] | arr2[i])[2:].zfill(n)
        answer.append(row.replace('1', '#').replace('0', ' '))
        
    return answer