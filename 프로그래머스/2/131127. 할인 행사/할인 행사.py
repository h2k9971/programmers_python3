def solution(want, number, discount):
    answer = 0
    want_food = dict(zip(want, number))
    count = sum(number)
    
    for num in range(len(discount) - count + 1): 
        new_discount = {}
            
        for food in discount[num:num+count]:
            if food in new_discount:
                new_discount[food] += 1
            else:
                new_discount[food] = 1
                
        if new_discount == want_food:
            answer += 1
        
    return answer