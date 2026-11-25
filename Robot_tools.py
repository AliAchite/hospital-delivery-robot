from collections import deque

def find_locations(hospital_map):
    start = None
    rooms = []
    for row in range(len(hospital_map)):
        for col in range(len(hospital_map[row])):
            cell = hospital_map[row][col]
            if cell == 'P':
                start = (row, col)
            elif type(cell) == str and cell.startswith('G'):
                rooms.append((row, col))
    return start, rooms

def find_shortest_path(hospital_map, start, goal):
    rows = len(hospital_map)
    cols = len(hospital_map[0]) 
    queue = deque([(start, [start])])
    visited = set() 
    
    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path
        visited.add(current)
        row, col = current

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            new_pos = (new_row, new_col)
            
            if 0 <= new_row < rows and 0 <= new_col < cols:
                if hospital_map[new_row][new_col] != 1 and new_pos not in visited:
                    queue.append((new_pos, path + [new_pos]))
    
    return None  