def solution(statues):
    statues.sort()
    count = 0
    for i in range(min(statues), max(statues)):
        if i not in statues:
            statues.append(i)
            count += 1
    statues.sort()
    return count

print(solution([6, 2, 3, 8]))