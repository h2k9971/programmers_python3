def solution(elements):
    answer = set()
    cir_elements = 2 * elements

    length = 1
    
    for i in range(len(elements)): # 길이가 1부터 n까지 

        for j in range(len(elements)): # 인덱스 번호 0 ~ n까지
            new_num = sum(cir_elements[j : j + length]) 
            
            if new_num not in answer:
                answer.add(new_num)
        
        length += 1 # 다음 길이

    return len(answer)