#
# sname="vikas"
# class student:
#     student_name="Vijay"
#     student_mobileno=9638527410
# print(sname)
# print(student.student_name)
# print(student.student_mobileno)

class student:
    sname="PWG"
    s_mno="9854547586"

    @staticmethod
    def showdata():
        print("Student name is",student.sname)
        print("Student mobile no is", student.s_mno)
student.showdata()