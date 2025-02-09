def load_flights():
    try:
        with open("flights\\flights.txt", "r") as file:
            flights = file.readlines()
        return flights
    except OSError as e:
        exit(f"OSError: {e}")

def load_bookings():
    try:
        with open("flights\\bookings.txt", "r") as file:
            bookings = file.readlines()
        return bookings
    except OSError as e:
        exit(f"OSError: {e}")

def main():
    flights = load_flights()
    bookings = load_bookings()
    grid = {}
    fail = {}
    for line in flights:
        parsed = line.split()
        flightID, plane, row, column = parsed[0].strip(), parsed[1].strip(), int(parsed[2].strip()), int(parsed[3].strip())
        grid[flightID] = [["-" for x in range(column)] for y in range(row)]
    for line in bookings:
        parsed = line.split()
        if parsed[0] == "BOOK":
            action, flight, name, surname, num_of_seats = parsed[0].strip(), parsed[1].strip(), parsed[2].strip(), parsed[3].strip(), int(parsed[4].strip())
            full_name = name + " " + surname
            available_seats = [(r, c) for r, ro in enumerate(grid[flight]) for c, seat in enumerate(ro) if seat == "-"]
            if len(available_seats) >= num_of_seats:
                for r, c in available_seats[:num_of_seats]:
                    grid[flight][r][c] = full_name
            else:
                fail[full_name] = [flight, num_of_seats]
        if parsed[0] == "CANCEL":
            action, flight, name, surname = parsed[0].strip(), parsed[1].strip(), parsed[2].strip(), parsed[3].strip()
            full_name = name + " " + surname
            positions = [(r, c) for r, ro in enumerate(grid[flight]) for c, seat in enumerate(ro) if seat == full_name]
            for r, c in positions:
                grid[flight][r][c] = "-"
    for key, (fl, num) in fail.items():
        print(f"BOOK {fl} {key} {num} - Fail ")

    print()

    for f, sigh in grid.items():
        print(f"Flight {f}:")
        row_index = 1
        for row in sigh:
            col_index = 1
            for seat in row:
                if seat != "-":
                    print(f"{row_index} {col_index} {seat}")
                col_index += 1
            row_index += 1
        print()

main()