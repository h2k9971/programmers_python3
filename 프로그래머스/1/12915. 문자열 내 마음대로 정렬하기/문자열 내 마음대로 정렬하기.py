def solution(strings, n):

    # (x[n], x) 튜플 형태로 반환 ('u' , 'sun')
    return sorted(strings, key = lambda x : (x[n], x))