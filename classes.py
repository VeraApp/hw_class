class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return "Ошибка"

    def _avggrade_(self):
        sum_grades = 0
        count_grades = 0
        for key, value in self.grades.items():
            count_grades += len(value)
            sum_grades += sum(value)
        return sum_grades / count_grades

    def __str__(self):
        avg_grade = self._avggrade_()
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {avg_grade}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        first_avg_grades = self._avggrade_()
        second_avg_grades = other._avggrade_()
        return first_avg_grades < second_avg_grades

    def __le__(self, other):
        first_avg_grades = self._avggrade_()
        second_avg_grades = other._avggrade_()
        return first_avg_grades <= second_avg_grades

    def __gt__(self, other):
        first_avg_grades = self._avggrade_()
        second_avg_grades = other._avggrade_()
        return first_avg_grades > second_avg_grades

    def __ge__(self, other):
        first_avg_grades = self._avggrade_()
        second_avg_grades = other._avggrade_()
        return first_avg_grades >= second_avg_grades

    def __ne__(self, other):
        first_avg_grades = self._avggrade_()
        second_avg_grades = other._avggrade_()
        return first_avg_grades != second_avg_grades

    def __eq__(self, other):
        first_avg_grades = self._avggrade_()
        second_avg_grades = other._avggrade_()
        return first_avg_grades == second_avg_grades


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []




class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _avggrade_(self):
        sum_grades = 0
        count_grades = 0
        for key, value in self.grades.items():
            count_grades += len(value)
            sum_grades += sum(value)
        return sum_grades / count_grades

    def __str__(self):
        avg_grade = self._avggrade_()

        return f"Имя: {self.name} \n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за лекции: {avg_grade}"

    def __lt__(self, other):
        first_avg_grades = self._avggrade_()
        second_avg_grades = other._avggrade_()
        return first_avg_grades < second_avg_grades

    def __le__(self, other):
        first_avg_grades = self._avggrade_()
        second_avg_grades = other._avggrade_()
        return first_avg_grades <= second_avg_grades

    def __gt__(self, other):
        first_avg_grades = self._avggrade_()
        second_avg_grades = other._avggrade_()
        return first_avg_grades > second_avg_grades

    def __ge__(self, other):
        first_avg_grades = self._avggrade_()
        second_avg_grades = other._avggrade_()
        return first_avg_grades >= second_avg_grades

    def __ne__(self, other):
        first_avg_grades = self._avggrade_()
        second_avg_grades = other._avggrade_()
        return first_avg_grades != second_avg_grades

    def __eq__(self, other):
        first_avg_grades = self._avggrade_()
        second_avg_grades = other._avggrade_()
        return first_avg_grades == second_avg_grades


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        #self.courses_attached = []
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}"


first_student = Student('Ruoy', 'Eman', 'your_gender')
first_student.courses_in_progress += ['Python', 'Pascal']

second_student = Student('Germiona', 'Granger', 'women')
second_student.courses_in_progress += ['Python', 'Java', 'C++']
second_student.finished_courses += ['Pascal', 'Basic']

first_lector = Lecturer('Robert', 'Langdon')
first_lector.courses_attached += ['Java Script']
first_lector.courses_attached += ['Python', 'Java']

second_lector = Lecturer('Filius', 'Flitwick')
second_lector.courses_attached += ['Python', 'Java', 'Ruby']


first_reviewer = Reviewer('Hardi', 'Neytonovich')
first_reviewer.courses_attached += ['Python']

second_reviewer = Reviewer('Severus', 'Snape')
second_reviewer.courses_attached += ['Python', 'Java', 'Java Script', 'C++']

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

print(first_student)
print(second_student)
print(first_lector)
print(second_lector)
print(first_reviewer)
print(second_reviewer)

print(first_student > second_student)
print(first_student >= second_student)
print(first_student < second_student)
print(first_student <= second_student)
print(first_student == second_student)
print(first_student != second_student)

print(first_lector > second_lector)
print(first_lector >= second_lector)
print(first_lector < second_lector)
print(first_lector <= second_lector)
print(first_lector == second_lector)
print(first_lector != second_lector)

