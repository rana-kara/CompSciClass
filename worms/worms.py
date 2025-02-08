from itertools import product

def load_file():
    try:
        with open("worms\seq.txt", "r") as file:
            data = file.readlines()
        return data
    except OSError as e:
        exit(f"OSError: {e}")

def check_rows(word1, word2, rowList):
    indices_word1 = [i for i, val in enumerate(rowList) if val == word1]
    indices_word2 = [i for i, val in enumerate(rowList) if val == word2]
    
    if not indices_word1 or not indices_word2:
        return False
    
    min_abs_difference = min(abs(a-b) for a, b in product(indices_word1, indices_word2))

    return min_abs_difference

def main():
    data = load_file()
    word1 = input("Enter your first word: ")
    word2 = input("Enter your second word: ")
    results_of_all_rows = {}
    for rowindex, row in enumerate(data):
        rowList = row.split()
        result_of_row = check_rows(word1, word2, rowList)
        if result_of_row is not False:

            if rowindex not in results_of_all_rows:
                results_of_all_rows[rowindex] = result_of_row
            else:
                results_of_all_rows[rowindex].append(result_of_row)
    if not results_of_all_rows:
        print("The two words never appear in the same sequence.")
    else:
        min_value = min(results_of_all_rows.values())
        key = [key for key, val in results_of_all_rows.items() if val == min_value]
        print(f"Min distance: sequence {key} (distance={min_value})")

main()