def load_seq():
    try:
        with open("munodi\seq.dat", "r") as file:
            seqData = file.readlines()
        return seqData
    except OSError as e:
        exit(f"OSError found: {e}")

def check_sequence(seq):
    is_valid = True
    if len(seq) == 1:
        return True
    for i in range(1, len(seq)):
        number = seq[i]
        prevNumber = seq[i-1]
        if (prevNumber % 2) == 0:
            if prevNumber//2 != number:
                is_valid = False
        if (prevNumber % 2) != 0:
            if (3*prevNumber)+1 != number:
                is_valid = False
    return is_valid

def main():
    seqData = load_seq()
    for index, row in enumerate(seqData):
        seq = list(int(num) for num in row.split())
        a = check_sequence(seq)

        if a:
            print(f"Sequence {index+1} is a Munodi sequence (length {len(seq)})")
        else:
            print(f"Sequence {index+1} is NOT a Munodi sequence")

main()