def load_moves():
    try:
        with open("connect-four\\moves.txt", "r") as file:
            moves = file.readlines()
        return moves
    except OSError as e:
        exit(f"OSError: {e}")

grid = [[["-"] for _ in range(7)] for _ in range(6)]

def main():
    moves = load_moves()
    player_1 = "G1"
    player_2 = "G2"
    print("Empty Grid")
    for b in grid:
        print("".join(item for sublist in b for item in sublist))
    print()
    for row in moves:
        splitted = row.split()
        player, column = splitted[0].strip(), int(splitted[1].strip())
        if player == player_1:
            for i in range(5, -1, -1):
                if grid[i][column][0] == "-":
                    grid[i][column][0] = "O"
                    print("Player G1 Plays")
                    for a in grid:
                        print("".join("".join(c[0]) for c in a))
                    print()
                    break
        elif player == player_2:
            for i in range(5, -1, -1):
                if grid[i][column][0] == "-":
                    grid[i][column][0] = "X"
                    print("Player G2 Plays")
                    for a in grid:
                        print("".join("".join(c[0]) for c in a))
                    print()
                    break

main()