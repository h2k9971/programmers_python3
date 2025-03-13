from functools import cmp_to_key

def compare(a, b):
    if a + b > b + a:
        return -1
    else:
        return 1

def solution(numbers):
    str_numbers = list(map(str, numbers)) # 숫자를 문자열로 변환
    sorted_numbers = sorted(str_numbers, key = cmp_to_key(compare)) 
    result = "".join(sorted_numbers)
    
    if result[0] == "0":
        return "0"
    
    return result