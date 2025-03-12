from fractions import Fraction
# from itertools import permutations

def solution(dots):
    answer = 0
    print(Fraction((dots[1][0] - dots[0][0]), (dots[1][1] - dots[0][1])))
    
    if Fraction((dots[1][0] - dots[0][0]), (dots[1][1] - dots[0][1])) == Fraction((dots[3][0] - dots[2][0]), (dots[3][1] - dots[2][1])):
        answer = 1
    elif Fraction((dots[2][0] - dots[0][0]), (dots[2][1] - dots[0][1])) == Fraction((dots[3][0] - dots[1][0]), (dots[3][1] - dots[1][1])):
        answer = 1
    elif Fraction((dots[3][0] - dots[0][0]), (dots[3][1] - dots[0][1])) == Fraction((dots[2][0] - dots[1][0]), (dots[2][1] - dots[1][1])):
        answer = 1
    else:
        answer = 0
    return answer