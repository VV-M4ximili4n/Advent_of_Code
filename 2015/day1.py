import os

with open(os.path.join(os.path.dirname(__file__), 'data/day1.txt'),'r') as file:
    for line in file:
        #line = '()())'
        floor = 0
        position = 0
        for direction in line:
            if direction == '(':
                floor += 1
                position += 1
            else:
                floor -= 1
                position += 1
    
            if floor == -1:
                break

        print(position)
        print(floor)