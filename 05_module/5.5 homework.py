""" 
1. calculator class to do add, deduct, multiply, divide
2. Pen class. create three object with different instance attribute
3. Exam attend_to_exam get_marks 
 """
#3
# ---------------
class student:
    def __init__(self, name):
        self.name= name
        self.marks=0 

    def attend_exam(self):
        print(f"{self.name} is attend the exam..")

    def get_marks(self, marks):
        self.marks=marks
        print(F"{self.name} got {self.marks} marks")

    def do_homework(self):
        print(f"{self.name} is doing homework.")
    
    def submit_project(self):
        print(f"{self.name} submiting the project.")
s1=student("habib")
s1.do_homework()
s1.attend_exam()
s1.get_marks(75)
