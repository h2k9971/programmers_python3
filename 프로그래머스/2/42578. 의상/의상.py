def solution(clothes):
    answer = 1
    dict = {}
    
    # 의상의 종류에 따른 딕셔너리 만들기
    for type1, type2 in clothes:
        
        if type2 in dict:
            dict[type2] += 1
        else:
            dict[type2] = 1
    
    for key in dict:
        answer = (dict[key] + 1) * answer
    
    return answer - 1