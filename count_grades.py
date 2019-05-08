def count_grades(grade_list,input_grade):
    grade_dictionary = {}
    for grade in grade_list:
        if grade not in grade_dictionary:
            grade_dictionary[grade] = 0
        grade_dictionary[grade] += 1
    print('There were',grade_dictionary[input_grade],input_grade+'\'s.')

input_list = input('Your all grade:\n')
user_grade = input('The grade you want to know:\n')
count_grades(input_list,user_grade)
