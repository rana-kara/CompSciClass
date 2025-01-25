

def load_file_data():

    try:
        with open("asciiart\landscape.txt", "r") as file:
            data = file.readlines()
        return data
    except OSError as error:
        exit(f"ERROR: {error}")

def check_if_coordinate_is_valid(data, x, y):

    try:
        line = data[y]

        terms = list(line.strip())

        term = terms[x]

        return True, term
    
    except:

        raise ValueError("That is not a valid coordinate in the file.")
    
def check_if_square_is_valid(data, x, y, square_size):

    try:

        square = []

        lastrownumber = x + square_size

        for i in range(y, y + square_size):
            line = data[i]

            terms = list(line.strip())

            row = terms[x:lastrownumber]

            if len(row) < square_size:
                raise ValueError("The square exceeds the available terms in the row.")

            square.append(row)

        return square
    
    except IndexError:
        raise ValueError("The square cannot be accessed completely due to exceeding file boundaries.")

def get_coordinates_and_square():
        data = load_file_data()
        while True:

            try:
                coordinate_input = input("Enter coordinates in an (x, y) format: ").strip()

                if not coordinate_input.startswith("(") and coordinate_input.endswith(")"):
                    raise ValueError("Input must be in the format (x, y)")
                
                coordinates = coordinate_input[1:-1].split(",")

                if len(coordinates) != 2:
                    raise ValueError("You can only input X and Y coordinates.")
                
                x = int(coordinates[0].strip())
                y = int(coordinates[1].strip())

                is_valid = check_if_coordinate_is_valid(data, x, y)

                while True:

                    try:

                        square_input = input ("Enter a number for square width&length: ").strip()

                        square_size = int(square_input)

                        square = check_if_square_is_valid(data, x, y, square_size)

                        print("The square is:")

                        for row in square:
                            print("".join(row))
                        return

                    except ValueError as e:
                        print(f"Error: {e}")
    
            except ValueError as e:
                print(f"Error: {e}")
        
get_coordinates_and_square()