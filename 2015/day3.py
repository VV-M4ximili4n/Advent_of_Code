import os

with open(os.path.join(os.path.dirname(__file__), 'data/day3.txt'),'r') as file:
    
    for line in file:
        
        santa_pos = (0, 0)
        robo_pos = (0, 0)
        visited = set()
        visited.add(santa_pos)  # beide starten am selben Ort

        for i, direction in enumerate(line):
            if i % 2 == 0:
                # Santa ist dran wenn index gerade
                x, y = santa_pos
            else:
                # Robo-Santa ist dran wenn index ungerade
                x, y = robo_pos

            if direction == '^':
                y += 1
            elif direction == 'v':
                y -= 1
            elif direction == '>':
                x += 1
            elif direction == '<':
                x -= 1

            new_pos = (x, y)
            visited.add(new_pos)

            if i % 2 == 0:
                santa_pos = new_pos
            else:
                robo_pos = new_pos

print(len(visited))









        #times_of_visited_locations = {}

        # for i in list_of_locations:
        #     if i in times_of_visited_locations:
        #         times_of_visited_locations[i] += 1
        #     else:
        #         times_of_visited_locations[i] = 1
        

        # count = sum(1 for i in times_of_visited_locations.values() if i >2)
        # print(count)