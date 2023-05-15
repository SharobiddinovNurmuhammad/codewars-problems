def solution(inputArray):
    arr = []
    for i in range(len(inputArray)-1):
        arr.append(inputArray[i] * inputArray[i+1])
    return max(arr)