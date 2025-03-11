def solution(s):
    answer = []
    is_first = True  # 단어의 첫 번째 문자인지 체크

    for i, alpha in enumerate(s):  
        
        if is_first and alpha.isalpha():  # 첫 알파벳이면 대문자로 변환
            answer.append(alpha.upper())
        else:
            answer.append(alpha.lower()) 
        
        is_first = alpha == " "  

    return "".join(answer) 