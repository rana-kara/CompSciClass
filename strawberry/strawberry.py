import string

def load_file():
    try:
        with open("strawberry\strawberry-short.txt", "r") as file:
            data = file.readlines()
        return data
    except OSError as e:
        exit(f"OSError: {e}")

def check_rows(cleanText):
    words = cleanText.split()
    finalList = []

    for i in range(len(words)-2):
        if len(words[i]) == len(words[i+1]) == len(words[i+2]):
            finalList.append((words[i].upper(), words[i+1].upper(), words[i+2].upper()))

    return finalList

def main():
    data = load_file()
    text = " ".join(data)
    translator = str.maketrans("", "", string.punctuation)
    cleanText = text.translate(translator)
    result = check_rows(cleanText)

    for triplet in result:
        print(triplet)

main()