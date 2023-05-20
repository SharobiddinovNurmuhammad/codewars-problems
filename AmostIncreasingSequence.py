def find_bad_pair(sequence):
    for i in range(0, len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            return i
        return -1
    
def almostInSeq(sequence):
    j = find_bad_pair(sequence)
    if j == -1:
        return True
    if find_bad_pair(sequence[j-1:j] + sequence[j+1:]) == -1:
        return True
    if find_bad_pair(sequence[j:j+1 + sequence[j+2:]]) == -1:
        return True
    return False

sequence = [1, 3, 2, 1]
print(almostInSeq(sequence))