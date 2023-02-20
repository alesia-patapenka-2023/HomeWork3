if __name__=='__main__':
    class Student:
        def __init__(self, student_id, first_name, last_name):
            self.student_id = student_id
            self.first_name = first_name
            self.last_name = last_name
            self.exam_scores = []

        def add_score(self, score):
            self.exam_scores.append(score)

        def show_scores(self):
            print(*self.exam_scores)

        def score_average(self):
            if not self.exam_scores:
                print("Студент еще не сдал ни одного экзамена")
                return
            average_score = sum(self.exam_scores) / len(self.exam_scores)
            print(f"Средний балл студента {self.first_name} {self.last_name} равен {average_score}")
            return average_score

        def course_passed(self):
            if len([score for score in self.exam_scores if score > 60]) >= 3:
                return True
            else:
                return False
    student1 = Student(1, "John", "Doe")
    student1.add_score(100)
    student1.add_score(95)
    student1.show_scores()
    student1.score_average()
    print(student1.course_passed())

    student2 = Student(2, "Linda", "Jones")
    student2.add_score(25)
    student2.add_score(65)
    student2.add_score(80)
    student2.add_score(75)
    student2.show_scores()
    student2.score_average()
    print(student2.course_passed())

    student3 = Student(3, "Jason", "Kirk")
    student3.add_score(50)
    student3.add_score(60)
    student3.add_score(55)
    student3.show_scores()
    student3.score_average()
    print(student3.course_passed())

    student4 = Student(4, "Jane", "Doe")
    student4.add_score(95)
    student4.add_score(80)
    student4.add_score(100)
    student4.show_scores()
    student4.score_average()
    print(student4.course_passed())