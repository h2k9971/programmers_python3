from collections import deque

def get_distance(pos1, pos2):
    
    distance = abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    
    return distance

def solution(numbers, hand):
    answer = ''
    queue_numbers = deque(numbers)
    dict_numbers = {1: 'L', 4: 'L', 7: 'L', 3: 'R', 6: 'R', 9: 'R'}
    phone_numbers = {
        1 : (0, 0), 2 : (0, 1), 3 : (0, 2),
        4 : (1, 0), 5 : (1, 1), 6 : (1, 2),
        7 : (2, 0), 8 : (2, 1), 9 : (2, 2),
        '*' : (3, 0), 0 : (3, 1), '#' : (3, 2)
    }
    # 초기 손가락 위치
    right_hand = '#'
    left_hand = '*'
    
    while queue_numbers: 
        number = queue_numbers.popleft()
        
        if number in dict_numbers: # 왼손 또는 오른손 고정 숫자
            hand_used = dict_numbers[number]
        else:
            left_distance = get_distance(phone_numbers[left_hand], phone_numbers[number]) # 이전 왼손의 위치와 비교
            right_distance = get_distance(phone_numbers[right_hand], phone_numbers[number]) # 이전 오른손의 위치와 비교
                
            if left_distance < right_distance:
                hand_used = 'L'
            elif left_distance > right_distance:
                hand_used = 'R'
            else:
                if hand == 'right':
                    hand_used = 'R'
                else:
                    hand_used = 'L'
                    
        answer += hand_used
        
        if hand_used == 'R':
            right_hand = number
        else:
            left_hand = number
            
    return answer