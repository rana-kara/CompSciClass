def load_file():
    try:
        with open("magic-boxes\\actions.txt", "r") as file:
            data = file.readlines()
        return data
    except OSError as e:
        exit(f"OSError: {e}")

def main():
    data = load_file()
    boxes = {}
    list_of_actors = ['Bob', 'Carl']
    for row in data:
        rowdata = row.split()
        actor, action, obj = rowdata[0].strip(), rowdata[1].strip(), rowdata[3].strip()
        if actor in list_of_actors:
            if len(boxes) < 42:
                if obj not in boxes:
                    if action == 'gives':
                        boxes[obj] = 1
                    elif action == 'takes':
                        exit(f"Action '{row.rstrip()}' cannot be performed.")
                elif obj in boxes:
                    if action == 'gives':
                        boxes[obj] += 1
                    elif action == 'takes':
                        if boxes[obj] > 0:
                            boxes[obj] -= 1
                            if boxes[obj] == 0:
                                del boxes[obj]
            elif len(boxes) == 42:
                exit(f"Action '{row.rstrip()}' cannot be performed.")
        else:
            exit(f"Action '{row.rstrip()}' cannot be performed.")

main()