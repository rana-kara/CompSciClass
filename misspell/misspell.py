def load_provided_file(file_path):
    try:
        with open(file_path, "r") as file:
            provided = file.readlines()
        return provided
    except OSError as e:
        exit(f"OSError: {e}")

def load_valid_misspells():
    try:
        with open("misspell\parole_italiane.txt", "r") as file:
            valid = file.readlines()
        return valid
    except OSError as e:
        exit(f"OSError: {e}")

def check_name(namelower):
    valid = load_valid_misspells()
    stuff = []
    for option in valid:
        option = option.strip()
        if len(namelower) == len(option) and sum(1 for c1, c2 in zip(namelower, option) if c1 != c2) == 1:
            stuff.append(option)
    return stuff

def main():
    file_path = input("Please input a file path: ")
    provided = load_provided_file(file_path)
    result_dict = {}
    for index, name in enumerate(provided):
        namelower = name.strip().lower()
        result = check_name(namelower)
        if result:
            result_dict[name.strip()] = result
        else:
            result_dict[name.strip()] = ["WARNING: No similar words were found!!!"]
    for i, variations in result_dict.items():
        print(f"Name: {i}")
        for a in variations:
            print(a)
        print()

main()