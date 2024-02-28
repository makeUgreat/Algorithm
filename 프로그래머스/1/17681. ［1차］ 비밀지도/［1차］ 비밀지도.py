def solution(n, arr1, arr2):
    answer = []
    
    for i,j in zip(arr1,arr2):
        comb = i | j        
        binary_key = bin(comb)[2:].rjust(n,'0')
        map_row = binary_key.replace('1','#').replace('0',' ')
        answer.append(map_row)
    
    return answer