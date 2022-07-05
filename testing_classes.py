from school import student
from school import classroom


student_1 = student(name = "my_name", last_name = "no")
student_2 = student(name = "my_name 222")

students = [student_1, student_2]

classroom1 = classroom(students)
classroom1.print_student_names()