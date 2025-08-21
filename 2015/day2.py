import os

with open(os.path.join(os.path.dirname(__file__), 'data/day2.txt'),'r') as file:
    total_surface = 0
    total_feet_of_ribbon = 0
    for line in file:
        l, w, h = map(int, line.strip().split('x'))
        side_areas = [l*w,w*h,h*l]

        sorted_list = sorted([l,w,h])
        feet_of_ribbon = 2*(sorted_list[0]+sorted_list[1]) + sorted_list[0] * sorted_list[1] * sorted_list[2]

        surface = 2*sum(side_areas)
        slack = min(side_areas)
        total_surface += surface+slack
        total_feet_of_ribbon += feet_of_ribbon

    
    print(total_feet_of_ribbon)