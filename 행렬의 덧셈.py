def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        sum = []
        for j in range(len(arr1[0])):
            sum.append(arr1[i][j] + arr2[i][j])
        answer.append(sum)
            
    return answer

import numpy as np

def solution(arr1, arr2):
    np_arr1 = np.array(arr1)
    np_arr2 = np.array(arr2)
    sum_arr = np_arr1 + np_arr2
    
    return sum_arr.tolist()