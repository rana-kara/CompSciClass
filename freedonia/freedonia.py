from datetime import datetime

def load_dates():
    try:
        with open("freedonia\\dates-example1.dat", "r") as file:
            date_data = file.readlines()
        return date_data
    except OSError as e:
        exit(f"OSError: {e}")

def load_rules():
    try:
        with open("freedonia\\rules-example1.dat", "r") as file:
            rules_data = file.readlines()
        return rules_data
    except OSError as e:
        exit(f"OSError: {e}")

def check(date):
    rules_data = load_rules()
    result_of_row = set()
    for row in rules_data:
        parsed = row.split(":")
        ruledate, rules = datetime.strptime(parsed[0].strip(), "%d-%m-%Y"), parsed[1].split()
        for rule in rules:
            strippedrule = rule.strip()
            if ruledate < date:
                if strippedrule.startswith("+"):
                    finalrule = strippedrule.removeprefix("+")
                    result_of_row.add(finalrule)
                elif strippedrule.startswith("-"):
                    finalrule = strippedrule.removeprefix("-")
                    result_of_row.discard(finalrule)
            elif ruledate > date:
                continue
    return result_of_row

def main():
    date_data = load_dates()
    for row in date_data:
        date = datetime.strptime(row.strip(), "%d-%m-%Y")
        result_of_row = check(date)
        if result_of_row:
            print(row.strip())
            print("\n".join(sorted(result_of_row)))
            print()
        else:
            print(row.strip())
            print()

main()