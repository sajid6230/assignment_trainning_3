from abc import ABC, abstractmethod

#abstract class School
class School(ABC):

#create abstract method Display
    @abstractmethod
    def Display(self):
        pass

#create a abstract method Update_details
    @abstractmethod
    def Update_details(self):
        pass

#Parent class Class ingerits from School
class Class(School):

    def __init__(self, Section_name : str, Class_teacher_name: str ):
        self.Section_name = Section_name
        self.Class_teacher_name = Class_teacher_name
    
    def Display(self):
        print(f'Section Name: {self.Section_name}')
        print(f'Class Teacher Name: {self.Class_teacher_name}') 
    

    def Update_details(self, Section_name = None, Class_teacher_name=None):
        if Section_name:
            self.Section_name = Section_name
        if Class_teacher_name:
            self.Class_teacher_name = Class_teacher_name

        print('Class Details Updated')

#child class Student from parent class Class 
class Student(Class):

    def __init__(self,Name: str ,Roll_No: int, Subject_marks : list, Section_name: str, Class_teacher_name: str):
        
        super().__init__(Section_name, Class_teacher_name)
        self.Name = Name
        self.Roll_No = Roll_No
        self.Subject_marks = Subject_marks
    
    def Display(self):
        super().Display()
        print(f"Student Name: {self.Name}")
        print(f"Roll No: {self.Roll_No}")
        print(f"Subject Marks: {self.Subject_marks}")
        print(f"Average Marks: {self.Calculate_avg()}")


#create method to calculate the average marks    
    def Calculate_avg(self):
        return sum(self.Subject_marks)/ len(self.Subject_marks)

    
    def Update_details(self,Name=None ,Roll_No=None, Subject_marks=None, Section_name=None, Class_teacher_name=None):
        if Name:
            self.Name = Name
        if Roll_No:
            self.Roll_No = Roll_No
        if Subject_marks:
            self.Subject_marks = Subject_marks
        if Section_name or Class_teacher_name:
            super().Update_details(Section_name, Class_teacher_name)

        print("Student details updated successfully")


#Creating an instance of Student
student1 = Student(Name='Sajid', Roll_No= 1, Subject_marks=[80,90,100],Section_name='Venus', Class_teacher_name='Mr John')

#display the student details
student1.Display()

#update the student details
student1.Update_details(Name='Sajid Ahmed', Section_name= 'Jupiter')

#after update display the student new datails
student1.Display()
