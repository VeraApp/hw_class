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



