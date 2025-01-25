import csv
from datetime import datetime

def load_csv_file():
    try:
        with open("soccer\player_stats.csv", "r", encoding="utf-8") as file:
            data = list(csv.reader(file))
            data = data[1:]
            return data
    except OSError as error:
        exit(f"ERROR: {error}")
    
def calculate_age(birth_year):
    age = 2022 - birth_year
    return age

    
def analyze_all_data():
    data = load_csv_file()

    forward_efficiency_by_nationality = {}
    midfield_efficiency_by_nationality = {}
    age_data = {}

    for row in data:

        try:
            nationality = (row[2])

            if nationality not in forward_efficiency_by_nationality:
                forward_efficiency_by_nationality[nationality] = []

            if nationality not in midfield_efficiency_by_nationality:
                midfield_efficiency_by_nationality[nationality] = []

            if float(row[4]) == 0 or float(row[8]) == 0:
                continue

            forward_efficiency = (float(row[5]) / float(row[4])) + (float(row[6]) / float(row[4])) - (float(row[5]) / float(row[4]))

            forward_efficiency_by_nationality[nationality].append(forward_efficiency)

            midfield_efficiency = (float(row[9])) + (float(row[12])) + (float(row[6])) / (float(row[8])) / float(row[4])

            midfield_efficiency_by_nationality[nationality].append(midfield_efficiency)

            birth_year = int(row[3])

            if nationality not in age_data:
                age_data[nationality] = []

            ages = calculate_age(birth_year)

            age_data[nationality].append(calculate_age(birth_year))


        except ValueError as e:
            print(f"ValueError processing row {row}: {e}")
        except ZeroDivisionError as e:
            print(f"ZeroDivisionError processing row {row}: {e}")

    average_age_data = {} 

    for nationality, ages in age_data.items():

        if nationality not in average_age_data:
            average_age_data[nationality] = []

        average_age_data[nationality] = sum(ages) / len(ages)

    three_lowest_avg_ages = sorted(average_age_data.items(), key=lambda x: x[1])[:3]

    national_efficiencies = {}
    for nationality, efficiencies in forward_efficiency_by_nationality.items():
        top_three_efficiencies = sorted(efficiencies, reverse=True)[:3]
        national_efficiencies[nationality] = sum(top_three_efficiencies)

    most_efficient_nationality = max(national_efficiencies.items(), key=lambda x: x[1])

    return forward_efficiency_by_nationality, midfield_efficiency_by_nationality, three_lowest_avg_ages, most_efficient_nationality

def format_and_print():
    (
        forward_efficiency_by_nationality,
        average_age_data,
        three_lowest_avg_ages,
        most_efficient_nationality,
    ) = analyze_all_data()

    print("The three nationalities with lower age average are:")
    for nationality, avg_age in three_lowest_avg_ages:
        print(f"{nationality:15}{avg_age:.2f} years")
    print()


    print("The nationality with the highest efficiency is:")
    print(most_efficient_nationality)

format_and_print()