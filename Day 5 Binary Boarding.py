# averiguar cual es tu asiento en el avion

import math

def getRow(boarding_pass):
    upperHalf = 127
    lowerHalf = 0
    operator = 128
    for item in boarding_pass[:6]:
        if item == 'F':
            upperHalf = upperHalf - operator/2
            operator = operator/2
        else:
            lowerHalf = lowerHalf + operator/2
            operator = operator/2

    if boarding_pass[6] == 'F':
        row = lowerHalf
    else:
        row = upperHalf

    upperHalf_seat = 0
    lowerHalf_seat = 7
    operator_seat = 8
    for item in boarding_pass[-3:9]:
        if item == 'R':
            upperHalf_seat = upperHalf_seat + operator_seat/2
            operator_seat = operator_seat/2
        else:
            lowerHalf_seat = lowerHalf_seat - operator_seat/2
            operator_seat = operator_seat/2

    if boarding_pass[9] == 'L':
        column = upperHalf_seat
    else:
        column = lowerHalf_seat

    return int((row * 8) + column)

with open('./files/day5.txt') as raw_input:
    boarding_pass = raw_input.read().split('\n')
    seats = [getRow(item) for item in boarding_pass]
    print(seats, max(seats))
    your_seat = [s for s in range(min(seats), max(seats)) 
            if s not in seats][0]
    print(f"Part 2: Your seat is {your_seat}")