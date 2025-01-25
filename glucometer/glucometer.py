def load_patient_data():
    try:
        with open("glucometer\\glucometers.txt", "r") as file:
            patient_data = file.readlines()
        return patient_data
    except OSError as error:
        exit(f"ERROR: {error}")

def analyze_data_and_print():
    patient_data = load_patient_data()

    general_data = {}

    for data in patient_data:
        parts = data.split(" ")

        patient, time, blood_sugar, temperature, heart_rate = parts[0], parts[1], parts[2], parts[3], parts[4]

        if int(blood_sugar) > 200:
            if patient not in general_data:
                general_data[patient] = []
            general_data[patient].append((time, int(blood_sugar)))

    for patient, record in general_data.items():
        sorted_records = sorted(record, key=lambda x:x[0], reverse=True)

        for time, blood_sugar in sorted_records:
            print(f"{patient} {time} {blood_sugar}")
        print()

analyze_data_and_print()