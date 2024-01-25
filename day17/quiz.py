words = ["apple","banana","cherry","date"]

def solution(arr):
    result = {}
    for i in arr:
        length = len(i)
        if  length in result:
            result[length] += 1
        else:
            result[length] = 1
    return result
a = solution(words)
print(a) # {5: 1, 6: 2, 4: 1}


