import classes

def avg_hw(list_students, course):
    sum_grades = 0
    count_grades = 0
    for student in list_students:
        if course in student.grades.keys():
            count_grades += len(student.grades[course])
            sum_grades += sum(student.grades[course])

    return sum_grades / count_grades

def avg_lec(list_lecturers, course):
    sum_grades = 0
    count_grades = 0
    for lecturer in list_lecturers:
        if course in lecturer.grades.keys():
            count_grades += len(lecturer.grades[course])
            sum_grades += sum(lecturer.grades[course])

    return sum_grades / count_grades

def main():
    # Инициализация студентов, лекторов и экспертов
    first_student = classes.Student('Ria', 'Eman', 'your_gender')
    first_student.courses_in_progress += ['Python', 'Pascal']

    second_student = classes.Student('Germiona', 'Granger', 'women')
    second_student.courses_in_progress += ['Python', 'Java', 'C++']
    second_student.finished_courses += ['Pascal', 'Basic']

    first_lector = classes.Lecturer('Robert', 'Langdon')
    first_lector.courses_attached += ['Java Script']
    first_lector.courses_attached += ['Python', 'Java']

    second_lector = classes.Lecturer('Filius', 'Flitwick')
    second_lector.courses_attached += ['Python', 'Java', 'Ruby']

    cool_mentor = classes.Mentor('Some', 'Buddy')
    cool_mentor.courses_attached += ['Python']

    first_reviewer = classes.Reviewer('Hardi', 'Neytonovich')
    first_reviewer.courses_attached += ['Python']

    second_reviewer = classes.Reviewer('Severus', 'Snape')
    second_reviewer.courses_attached += ['Python', 'Java', 'Java Script', 'C++']

    # Проставление оценок студентам от экспертов за домашнее задание
    first_reviewer.rate_hw(first_student, 'Python', 8)
    first_reviewer.rate_hw(first_student, 'Java', 3)
    first_reviewer.rate_hw(first_student, 'Python', 6)
    first_reviewer.rate_hw(first_student, 'Python', 10)
    second_reviewer.rate_hw(first_student, 'Python', 4)
    second_reviewer.rate_hw(first_student, 'C++', 6)
    second_reviewer.rate_hw(first_student, 'Python', 3)
    second_reviewer.rate_hw(first_student, 'Python', 0)

    first_reviewer.rate_hw(second_student, 'Python', 10)
    first_reviewer.rate_hw(second_student, 'Python', 10)
    first_reviewer.rate_hw(second_student, 'Python', 8)
    first_reviewer.rate_hw(second_student, 'Python', 10)
    second_reviewer.rate_hw(second_student, 'Python', 7)
    second_reviewer.rate_hw(second_student, 'Python', 6)
    second_reviewer.rate_hw(second_student, 'Python', 9)
    second_reviewer.rate_hw(second_student, 'Java', 10)
    second_reviewer.rate_hw(second_student, 'C++', 9)
    second_reviewer.rate_hw(second_student, 'Java', 7)
    second_reviewer.rate_hw(second_student, 'C++', 9)

    # Проставление оценок лекторам за лекции от студентов
    first_student.rate_lec(first_lector, 'Java', 8)
    first_student.rate_lec(first_lector, 'Python', 7)
    first_student.rate_lec(first_lector, 'Python', 10)
    first_student.rate_lec(first_lector, 'Pascal', 8)
    first_student.rate_lec(first_lector, 'Java Script', 6)
    first_student.rate_lec(second_lector, 'Python', 4)
    first_student.rate_lec(second_lector, 'Python', 2)
    first_student.rate_lec(second_lector, 'Pascal', 10)
    first_student.rate_lec(second_lector, 'Python', 5)

    second_student.rate_lec(first_lector, 'Java', 6)
    second_student.rate_lec(first_lector, 'Python', 5)
    second_student.rate_lec(first_lector, 'Pascal', 3)
    second_student.rate_lec(first_lector, 'Java', 8)
    second_student.rate_lec(second_lector, 'Java', 8)
    second_student.rate_lec(second_lector, 'Python', 10)
    second_student.rate_lec(second_lector, 'Python', 9)

    # Вывод данных
    print(first_student)
    print(second_student)
    print(first_lector)
    print(second_lector)
    print(first_reviewer)
    print(second_reviewer)

    # Сравнение студентов
    print('Сравнение студентов:')
    print(f'Оператор больше: {first_student > second_student}')
    print(f'Оператор больше и равно: {first_student >= second_student}')
    print(f'Оператор меньше: {first_student < second_student}')
    print(f'Оператор меньше и равно: {first_student <= second_student}')
    print(f'Оператор равно: {first_student == second_student}')
    print(f'Оператор не равно: {first_student != second_student}')

    # Сравнение лекторов
    print('Сравнение лекторов:')
    print(f'Оператор больше: {first_lector > second_lector}')
    print(f'Оператор больше и равно: {first_lector >= second_lector}')
    print(f'Оператор меньше: {first_lector < second_lector}')
    print(f'Оператор меньше и равно: {first_lector <= second_lector}')
    print(f'Оператор равно: {first_lector == second_lector}')
    print(f'Оператор не равно: {first_lector != second_lector}')

    # Подсчет средней оценки за домашние задания по всем студентам в рамках конкретного курса
    list_students = [first_student, second_student]
    course = 'Python'
    avg_grades_hw = avg_hw(list_students, course)
    print(f'Средння оценка за домашнее задание по всем студентам за курс {course}: {avg_grades_hw}')

    # Подсчет средней оценки за лекции всех лекторов в рамках курса
    list_lecturers = [first_lector, second_lector]
    avg_grades_lec = avg_lec(list_lecturers, course)
    print(f'Средння оценка за лекции всех лекторов за курс {course}: {avg_grades_lec}')

if __name__ == "__main__":
    main()