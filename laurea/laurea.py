def load_exams():
    try:
        with open("laurea\exams.log", "r") as file:
            examdata = file.readlines()
        return examdata
    except OSError as error:
        exit(f"OSError: {error}")

def load_cfu():
    try:
        with open("laurea\cfu.dat", "r") as file:
            cfudata = file.readlines()
        return cfudata
    except OSError as error:
        exit(f"OSError: {error}")

def check_if_appropriate(student, data):
    cfudata = load_cfu()

    cfu_info = {}
    for row in cfudata:
        parts = row.strip().split(",")
        exam_code, cfu, mandatory = parts[0], int(parts[1]), bool(int(parts[2]))
        cfu_info[exam_code] = {"cfu": cfu, "mandatory": mandatory}

    passed_students = {}

    for student, exams in data.items():
        total_credits = 0
        mandatory_credits = 0
        weighted_sum = 0
        total_cfu_for_average = 0

        last_attempts = {}
        for exam in exams:
            exam_code, grade = exam["exam_examdata"], exam["grade"]
            if grade in {"A", "R"}:
                continue

            if exam_code not in last_attempts or grade > last_attempts[exam_code]:
                last_attempts[exam_code] = grade

        for exam_code, grade in last_attempts.items():
            cfu = cfu_info[exam_code]["cfu"]
            mandatory = cfu_info[exam_code]["mandatory"]

            if grade == "30L":
                grade = 33
            else:
                grade = int(grade)

            total_credits += cfu
            weighted_sum += grade * cfu
            total_cfu_for_average += cfu
            if mandatory:
                mandatory_credits += cfu

        if total_credits >= 30 and mandatory_credits >= 10:
            gpa = weighted_sum / total_cfu_for_average
            passed_students[student] = {
                "total": total_credits,
                "mandatory": mandatory_credits,
                "gpa": gpa
            }

    return passed_students

def main():
    examdata = load_exams()

    data = {}

    for row in examdata:
        parts = row.strip().split(",")
        student, date, exam_examdata, grade = parts[0], parts[1], parts[2], parts[3]

        if student not in data:
            data[student] = []
        data[student].append({
            "date": date,
            "exam_examdata": exam_examdata,
            "grade": grade
        })

    passed_students = check_if_appropriate(student, data)

    for student, info in passed_students.items():
        print(f"STUDENT {student}")
        print(
            f"Student with {info['total']} total credits; "
            f"{info['mandatory']} mandatory credits; {info['gpa']:.2f} average."
        )
        print()

main()