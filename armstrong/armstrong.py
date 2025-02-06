def read_numbers():
    try:
        with open("armstrong\\numbers.txt", "r") as file:
            numberdata = file.readlines()
        return numberdata
    except OSError as e:
        exit(f"OSError found: {e}")

def save(list_of_numbers):
    try:
        with open("armstrong\\armstrong.txt", "w") as file:
            for number in list_of_numbers:
                file.write(number + "\n")
    except OSError as e:
        exit(f"OSError found: {e}")

            

def main():
    numberdata = read_numbers()
    list_of_numbers = []
    for row in numberdata:
        row = row.strip()
        chars = list(row)
        x = int(0)
        rowfinal = int(row)
        for a in chars:
            x += pow(int(a), len(row))
        if x == rowfinal:
            list_of_numbers.append(row)

    save(list_of_numbers)

main()