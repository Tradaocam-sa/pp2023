
import numpy as np


class Courses:
    def __init__(self, Course_ID, Course_Name):
        self.__course_mark = {}
        self.__Course_ID = Course_ID
        self.__Course_Name = Course_Name
    def get_Course_ID(self):
        return self.__Course_ID
    def get_Course_Name(self):
        return self.__Course_Name
    def set_Course_ID(self, Course_ID):
        self.__Course_ID = Course_ID
    def set_Course_Name(self, Course_Name):
        self.__Course_Name = Course_Name
    def get_course(self):
        return f'ID: {self.__Course_ID } Name: {self.__Course_Name}'
    def set_mark(self, course_mark, ID): 
        self.__course_mark[ID] = course_mark
    def get_mark(self, Student_id):
        return self.__course_mark[Student_id]

   


class Students:
    def __init__(self,  ID, name, DoB ):
        self.__GPA = []
        self.__ID = ID
        self.__name = name
        self.__DoB = DoB
    def get_ID(self):
        return self.__ID
    def get_name(self):
        return self.__name
    def get_DoB(self):
        return self.__DoB
    def set_ID(self, ID):
        self.__ID = ID
    def set_name(self, name):
        self.__name = name
    def set_DoB(self, DoB):
        self.__DoB = DoB
    def get_student(self):
        return f'ID: {self.__ID}  Name: {self.__name}  DoB:{self.__DoB}'
    def set_GPA(self,  mark):
        self.__GPA.append(mark)
    def get_GPA(self):
        return np.average(self.__GPA)

        


          
if __name__ == '__main__':
    Students_List, Course_List = [], []
    
    
    
    number_of_student = int(input("Number of Students: "))  #Type inforamtion of Students
    for i in range(number_of_student) :
        print("Information of Student" + str(i+1) + ": ")
        student_id = input("Student ID: ")
        student_name = input("Student name: ")
        DoB = input("DoB: ")
        student = Students(student_id, student_name, DoB)
        
        Students_List.append(student)

    print("Information about students: ")   
    
    
    
    
    for i in range(number_of_student):    #Print Student's informations
        print(Students_List[i].get_student())
        
    number_of_course = int(input("Number of courses: "))
    for i in range(number_of_course):
        print("Information of course "+ str(i+1) + ':')
        course_id = input("Course ID: ")
        course_name = input("Course name: ")
        course = Courses(course_id, course_name)
        Course_List.append(course)
        
        
        
    print("Information of courses: ") #print course's informations
    for i in range(number_of_course):
        print(Course_List[i].get_course())
    
    
    
    
    for i in range(len(Course_List)):   #Funtion for input mark of student in each course:
            
            print(f' course {Course_List[i].get_Course_Name()}')
            for j in range(len(Students_List)):
                student_mark = int(input(f'Mark of {Students_List[j].get_name()}: '))
                Course_List[i].set_mark(student_mark,Students_List[j].get_ID())

    
    for i in range(len(Students_List)):    #print mark of students in each course:
            print(f'Student: {Students_List[i].get_name()}')
            for j in range(len(Course_List)):
                print(f'{Course_List[j].get_Course_Name()}:{Course_List[j].get_mark(Students_List[i].get_ID())}')
        
        
    for i in range(len(Students_List)):
        for j in range(len(Course_List)):
            Students_List[i].set_GPA(Course_List[j].get_mark(Students_List[i].get_ID())) 
                

    Students_List.sort( key = lambda Students_List : Students_List.get_GPA()) 

    print("List of student's average grade:")

    for i in range(len(Students_List)):
        print(f'{Students_List[i].get_name()}: {Students_List[i].get_GPA()}')



        
        
    
            
       

    
    
    
        