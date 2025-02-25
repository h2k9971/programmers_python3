def solution(wallet, bill):
    answer = 0 #1
    
    while min(bill) > min(wallet) or max(bill) > max(wallet): #2
        
        if bill[0] > bill[1]: #2-1
            bill[0] //= 2 
            
        else:
            bill[1] //= 2 #2-2
            
        answer += 1 #2-3
    
    return answer #3