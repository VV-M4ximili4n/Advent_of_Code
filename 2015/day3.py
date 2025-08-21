import os

with open(os.path.join(os.path.dirname(__file__), 'data/day3.txt'),'r') as file:
    
    for line in file:
        list_of_locations = []
        times_of_visited_locations = {}
        x = 0
        y = 0
        for direction in line:
            
            if direction == '^':
                y += 1
            elif direction == 'v':
                y -= 1
            elif direction == '>':
                x += 1
            elif direction == '<':
                x -= 1
            list_of_locations.append((x,y))
        
        for i in list_of_locations:
            if i in times_of_visited_locations:
                times_of_visited_locations[i] += 1
            else:
                times_of_visited_locations[i] = 1
        

        count = sum(1 for i in times_of_visited_locations.values() if i >2)
        print(count)