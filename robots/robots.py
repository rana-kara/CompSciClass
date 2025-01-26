def load_trajectories():
    try:
        with open("robots\\trajectories.txt", "r") as file:
            trajectories = file.readlines()
        return trajectories
    except OSError as error:
        exit(f"OSError found: {error}")

def parse_mov(mov_seq):
    mov_seq = mov_seq.strip()
    moves = []
    for i in range(0, len(mov_seq), 2):
        move = (mov_seq[i], mov_seq[i+1])
        moves.append(move)
    return moves

def count_visited_boxes(x, y, moves):
    x, y = int(x), int(y)
    visited = set()
    visited.add((x, y))

    for direction, axis in moves:
        if axis == "h":
            if direction == "+":
                x += 1
            elif direction == "-":
                x -= 1
        elif axis == "v":
            if direction == "+":
                y += 1
            elif direction == "-":
                y -= 1
        visited.add((x, y))

    return visited

def main():
    trajectories = load_trajectories()
    robot_paths = {}
    for row in trajectories:

        parts = row.split()

        robot_id, x, y, mov_seq = parts[0], parts[1], parts[2], parts[3]

        moves = parse_mov(mov_seq)

        robot_id = robot_id.upper()

        visited = count_visited_boxes(x, y, moves)

        robot_paths[robot_id] = visited

    robot1 = input("Enter first robot name: ").strip()
    robot2 = input("Enter second robot name: ").strip()

    if robot1.upper() in robot_paths and robot2.upper() in robot_paths:
        common_boxes = robot_paths[robot1.upper()].intersection(robot_paths[robot2.upper()])
        print(f"The number of boxes visited by both robots is: {len(common_boxes)}")
    else:
        print("One or both of the robot names are invalid.")

main()