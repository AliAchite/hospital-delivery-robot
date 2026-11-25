from map_data import HOSPITAL_MAP
from Robot_tools import find_locations, find_shortest_path

def get_nearest_room(hospital_map, current_pos, rooms):
    best_room = None
    best_path = None
    for room in rooms:
        path = find_shortest_path(hospital_map, current_pos, room)
        if path and (best_path is None or len(path) < len(best_path)):
            best_path = path
            best_room = room
            
    return best_room, best_path


def start_robot():
    print("The robot has started its work \n")
    start_pos, rooms = find_locations(HOSPITAL_MAP)
    current_pos = start_pos
    total_cost = 0
    visited_rooms = []
    while rooms:
        target_room, path = get_nearest_room(HOSPITAL_MAP, current_pos, rooms)
        
        if not path:
            print(f"there is no path to the room{target_room}!")
            if target_room in rooms:
             rooms.remove(target_room)
            continue
        
        step_cost = len(path) - 1 
        total_cost += step_cost
        
        print(f"the robot is going to the room{target_room} |step counter: {step_cost}")
        print(f"path: {path}\n")
        
        current_pos = target_room
        rooms.remove(target_room)
        visited_rooms.append(target_room)

    print("=" * 40)
    print(f"visits: {visited_rooms}")
    print(f"Total Cost: {total_cost}")

if __name__ == "__main__":
    start_robot()