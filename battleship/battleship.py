def read_map():
    try:
        with open("battleship\\map1.dat", "r") as file:
            map = file.readlines()
        return map
    except OSError as e:
        exit(f"OSError: {e}")

def read_moves(moves_path):
    try:
        with open(moves_path, "r") as file:
            moves = file.readlines()
        return moves
    except OSError as e:
        exit(f"OSError: {e}")

letters_to_index = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9
}

updated_map = read_map()

def check(move):
    map = read_map()
    coords = move.split(",")
    x_coord, y_coord = coords[0].strip(), int(coords[1].strip())
    if x_coord in letters_to_index and y_coord <= 10:
        row = map[y_coord-1]
        x_correspondant = letters_to_index[x_coord]
        shot = row[x_correspondant]
        if shot == "-":
            u = list(updated_map[y_coord-1])
            u[x_correspondant] = "o"
            updated_map[y_coord-1] = "".join(u)
            miss = "miss"
            return miss
        elif shot == "#":
            u = list(updated_map[y_coord-1])
            u[x_correspondant] = "*"
            updated_map[y_coord-1] = "".join(u)
            hit = "hit"
            return hit

def main():
    moves_path = input("Enter the path of the file containing moves: ")
    moves = read_moves(moves_path)
    for index, move in enumerate(moves):
        result = check(move)
        if (index % 2) == 0:
            player = "Player 1"
        elif (index % 2) != 0:
            player = "Player 2"

        print(player)
        print(move.rstrip())
        print(result)
        print()

    for index, row in enumerate(updated_map):
        row_list = list(row.strip())
        for charindex, char in enumerate(row_list):
            if char == "#":
                row_list[charindex] = "-"
        updated_map[index] = "".join(row_list)
    for item in updated_map:
        print(item.strip())

main()