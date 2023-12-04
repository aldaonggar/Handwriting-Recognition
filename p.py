import math


def solution(area):
    output = []    
    while(area):
        if (area <= 0):
            break
        temp = int(math.sqrt(area))
        output.append(temp**2)
        area -= temp**2
    return output
    
print(solution(15324))
