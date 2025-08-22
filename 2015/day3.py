import os

with open(os.path.join(os.path.dirname(__file__), 'data/day3.txt'),'r') as file:
    
    for line in file:
        intervalle = [2, -2]
        num_location = 0
        list_of_locations = set()
       
        for i in intervalle:
            x = 0
            y = 0
              
            for direction in line[::i]:
                
                if direction == '^':
                    y += 1
                elif direction == 'v':
                    y -= 1
                elif direction == '>':
                    x += 1
                elif direction == '<':
                    x -= 1
                list_of_locations.add((x,y))
                print((x,y))       
        print(len(list_of_locations))  








        #times_of_visited_locations = {}

        # for i in list_of_locations:
        #     if i in times_of_visited_locations:
        #         times_of_visited_locations[i] += 1
        #     else:
        #         times_of_visited_locations[i] = 1
        

        # count = sum(1 for i in times_of_visited_locations.values() if i >2)
        # print(count)