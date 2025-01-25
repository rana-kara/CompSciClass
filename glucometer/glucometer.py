def load_patient_data():
    try:
        with open("glucometer\glucometers.txt", "r") as file:
            patient_data = file.readlines()
        return patient_data
    except OSError as error:
        exit(f"ERROR: {error}")

def analyze_data_and_print():
    patient_data = load_patient_data()