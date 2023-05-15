'''
Given a year, return the century it is in. The first c
entury spans from the year 1 up to and including the year 100, 
the second - from the year 101 up to and including the year 200, etc.
'''

def solution(year):
    if year % 100 == 0:
        return year // 100
    else:
        return (year // 100) + 1