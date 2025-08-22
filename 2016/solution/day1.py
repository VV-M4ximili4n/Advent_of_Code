import os

with open(os.path.join(os.path.dirname(__file__), '../data/day1.txt'),'r') as file:
    for line in file:
        x,y = 0,0
        direction = 0 # 0=N, 1=E, 2=S, 3=W
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] #definiert die Himmelsrichtungen norden, osten im koordinaten system
        for instrution in line.strip().split(', '):
            #print(direction[0] == 'R')
            
            turn = instrution[0]
            steps = int(instrution[1:])
            
            if turn == 'R':
                direction = (direction + 1) % 4
            
            if turn == 'L':
                direction = (direction - 1) % 4
            
            dx, dy = directions[direction]
           

            
            dx, dy = directions[direction]
            x += dx * steps
            y += dy * steps

        print(abs(x) + abs(y))
        


print(2%4)