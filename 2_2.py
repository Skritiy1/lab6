'''2. Составить программу для обработки результатов кросса на 500 м для женщин.
Для каждой участницы ввести фамилию, группу, фамилию преподавателя, результат.
Получить результирующую таблицу, упорядоченную по результатам, в которой содержится также
информация о выполнении норматива.
Определить суммарное количество участниц, выполнивших норматив.'''
class Student:
    def __init__(self, name):
        self.name = name
        self.math_score = 0
        self.physics_score = 0
        self.russian_score = 0
    
    def set_scores(self, math, physics, russian):
        self.math_score = math
        self.physics_score = physics
        self.russian_score = russian
    
    def is_expelled(self):
        return (self.math_score == 2 or 
                self.physics_score == 2 or 
                self.russian_score == 2)
    
    def average_score(self):
        return (self.math_score + self.physics_score + self.russian_score) / 3

class Group:
    def __init__(self):
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
    
    def get_successful_students(self):
        successful_students = [
            student for student in self.students 
            if not student.is_expelled()
        ]
        
        return sorted(
            successful_students, 
            key=lambda x: x.average_score(), 
            reverse=True
        )
#Здесь можно менять данные об учениках
def main():
    group = Group()

    student1 = Student("Иван")
    student1.set_scores(4, 5, 4)
    group.add_student(student1)

    student2 = Student("Мария")
    student2.set_scores(5, 5, 5)
    group.add_student(student2)

    student3 = Student("Петр")
    student3.set_scores(2, 4, 3)
    group.add_student(student3)

    student4 = Student("Анна")
    student4.set_scores(4, 4, 4)
    group.add_student(student4)

    print("Оценки учеников:")
    for student in group.students:
        print(f"{student.name}:")
        print(f"  Математика: {student.math_score}")
        print(f"  Физика: {student.physics_score}")
        print(f"  Русский язык: {student.russian_score}")
        print(f"  {'Отчислен' if student.is_expelled() else 'Допущен к дальнейшему обучению'}")
        print()

    successful_students = group.get_successful_students()
    
    print("Список успешно сдавших экзамены (в порядке убывания среднего балла):")
    for student in successful_students:
        print(f"{student.name}: Средний балл = {student.average_score():.2f}")

if __name__ == "__main__":
    main()