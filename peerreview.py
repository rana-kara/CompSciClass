def letter_to_grade(letter_grade):
    base_grades = {
        'A': 4.0,
        'B': 3.0,
        'C': 2.0,
        'D': 1.0,
        'F': 0.0
    }
    
    if len(letter_grade) == 1:
        grade_letter = letter_grade
        modifier = ''
    elif len(letter_grade) == 2:
        grade_letter = letter_grade[0]
        modifier = letter_grade[1]
    else:
        return "Invalid grade format."
    
    if grade_letter not in base_grades:
        return "Invalid letter grade."
    
    if modifier and modifier not in ['+', '-']:
        return "Invalid modifier."
    
    if grade_letter == 'F' and modifier in ['+', '-']:
        return "That grade does not exist."
    
    numeric_grade = base_grades[grade_letter]
    
    if modifier == '+':
        if grade_letter != 'A':
            numeric_grade += 0.3
    elif modifier == '-':
        numeric_grade -= 0.3    
    
    return numeric_grade

user_input = input("Enter a letter grade with or without a modifier: ")
numeric_value = letter_to_grade(user_input)

if isinstance(numeric_value, float):
    print(f"The numerical value of {user_input} is {numeric_value}.")
else:
    print(numeric_value)


