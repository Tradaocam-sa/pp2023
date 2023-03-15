class Courses:
    def __init__(self, Course_ID, Course_Name):
        
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
   


class Students:
    def __init__(self,  ID, name, DoB ):
         
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
    
class Mark:
    def __init__(self, mark):
        self.__mark = mark
    def get_mark(self):
        return f'Mark {self.__mark}'
          
if __name__ == '__main__':
    Students_List, Course_List = [], []
    Student_in_course, Course_taken = [], []
    Grade = []
    number_of_student = int(input("Number of Students: "))
    for i in range(number_of_student) :
        print("Information of Student" + str(i+1) + ": ")
        student_id = input("Student ID: ")
        student_name = input("Student name: ")
        DoB = input("DoB: ")
        x = Students(student_id, student_name, DoB)
        Student_in_course.append(student_name)
        Students_List.append(x.get_student())
    print("Information about students: ")   
    for i in range(number_of_student):
        print(Students_List[i])
        
    number_of_course = int(input("Number of courses: "))
    for i in range(number_of_course):
        print("Information of course "+ str(i+1) + ':')
        course_id = input("Course ID: ")
        course_name = input("Course name: ")
        y = Courses(course_id, course_name)
        Course_List.append(y.get_course())
        Course_taken.append(course_name)
    print("Information of courses: ") 
    for i in range(number_of_course):
        print(Course_List[i])
    
    
    
    course = int(input("Choose the course number: "))
    
    for j in range(number_of_course):
        if j + 1 == course:
            print(f'Choose course {Course_taken[j]}')
            for i in range(len(Student_in_course)):
                student_mark = int(input(f'Mark of {Student_in_course[i]} :'))
                # Grade = Mark(student_mark)
                Grade.append(student_mark)
                
    for i in range(number_of_student):
        print(f'Mark of {Student_in_course[i]} : {Grade[i]} ')

    
    
    
        