def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        new_array = []
        sorted_array = []
        start = commands[i][0] 
        end = commands[i][1]
        k = commands[i][2] 
        new_array = array[start - 1:end]
        sorted_array = sorted(new_array)
        answer.append(sorted_array[k - 1])
        
    return answer