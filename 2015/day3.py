# import os

# with open(os.path.join(os.path.dirname(__file__), 'data/day3.txt'),'r') as file:
    
#     for line in file:
#         start_index = [0, 1]
#         num_location = 0
#         list_of_locations = set()
       
#         for i in start_index:
#             x = 0
#             y = 0
#             list_of_locations.add((x,y)) #start location
#             for direction in line[i::2]:
                
#                 if direction == '^':
#                     y += 1
#                 elif direction == 'v':
#                     y -= 1
#                 elif direction == '>':
#                     x += 1
#                 elif direction == '<':
#                     x -= 1
#                 list_of_locations.add((x,y))
#         print(list_of_locations)       
#         print(len(list_of_locations))  


print(97%5)





        #times_of_visited_locations = {}

        # for i in list_of_locations:
        #     if i in times_of_visited_locations:
        #         times_of_visited_locations[i] += 1
        #     else:
        #         times_of_visited_locations[i] = 1
        

        # count = sum(1 for i in times_of_visited_locations.values() if i >2)
        # print(count)