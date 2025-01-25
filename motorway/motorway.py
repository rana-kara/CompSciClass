def load_car_data():
    try:
        with open("motorway\\cars.txt", "r") as file:
            cardata = file.readlines()
        return cardata
    
    except OSError as error:
        exit(f"ERROR: {error}")

def load_toll_data():
    try:
        with open("motorway\\toll.txt", "r") as file:
            tolldata = file.readlines()
        return tolldata
    except OSError as error:
        exit(f"ERROR: {error}")

def analyze_and_print_all_data():
    cardata = load_car_data()
    tolldata = load_toll_data()

    toll_data = {}

    for row in tolldata:
        parts = row.strip().split(";")

        tollentrance, tollexit, toll = parts[0], parts[1], float(parts[2])

        toll_data[(tollentrance, tollexit)] = toll
        toll_data[(tollexit, tollentrance)] = toll

    license_plate_classification = {}

    for row in cardata:

        parts = row.strip().split(";")

        license_plate, entrance, exit, date = parts[0], parts[1], parts[2], parts[3]

        if license_plate not in license_plate_classification:
            license_plate_classification[license_plate] = {
                "total_toll": 0,
                "number_of_sections": 0,
                "number_of_distinct_entrances": set()
            }

        if (entrance, exit) in toll_data or (exit, entrance) in toll_data:
            toll = toll_data.get((entrance, exit)) or toll_data.get((exit, entrance))
            license_plate_classification[license_plate]["total_toll"] += toll
            license_plate_classification[license_plate]["number_of_sections"] += 1
            license_plate_classification[license_plate]["number_of_distinct_entrances"].add((entrance, exit))
        else:
            print(f"Route not found in toll data: {entrance} to {exit}")

    for license_plate, data in license_plate_classification.items():
        data["number_of_distinct_entrances"] = len(data["number_of_distinct_entrances"])

    highest_paying_plate = max(license_plate_classification.items(), key=lambda x: x[1]["total_toll"])

    plate, details = highest_paying_plate

    for license_plate, data in license_plate_classification.items():
        print(f"License Plate: {license_plate}, {data["total_toll"]:.2f} toll paid, {data["number_of_distinct_entrances"]} distinct entrances made over a total of {data["number_of_sections"]}")
    print(f"The license plate with the highest toll paid is {plate} with {details["total_toll"]} toll")

analyze_and_print_all_data()