def solution(a, b, c, d):
    answer = 0
    arr = [a,b,c,d]
    cnt = []
    
    for i in arr:
        cnt.append(arr.count(i))
    
    if max(cnt) == 4:
        answer = 1111 * a
        
    elif max(cnt) == 3:
        answer = (10 * arr[cnt.index(3)] + (arr[cnt.index(1)])) ** 2
                
    elif max(cnt) == 2:
        if 1 in cnt:
            answer = arr[cnt.index(1)] * arr[cnt.index(1, cnt.index(1)+1, 4)]
                  
        else:
            for i in arr:
                if a != i:
                  answer = (a + i) * abs(a - i)
    else:
        answer = min(arr)
    
    return answer