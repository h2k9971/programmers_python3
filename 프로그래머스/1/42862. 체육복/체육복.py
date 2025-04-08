def solution(n, lost, reserve):
    
    s = set(lost) & set(reserve)
    l = set(lost) - s  #체육복 빌릴 필요가 없음
    r = set(reserve) - s
    
    for x in sorted(r):
        if x - 1 in l:
            l.remove(x - 1)
        elif x + 1 in l:
            l.remove(x + 1)
    
    return n - len(l)