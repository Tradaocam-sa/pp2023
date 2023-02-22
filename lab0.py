n = int(input("Number of students: "))
m = int(input("Number of course "))

lsv = []
for i in range(0, n, 1):
    print("Information of student no " +str(i + 1))
    stdId= input("Student ID: ")
    stdName= input("Name of student: ")
    major = input("Class: ")
    d = {"Student ID": stdId,
         "Student name": stdName,
         "Dob" : major,
         }
    lsv.append(d)

print("No \t Student ID\t Student name\t DoB")
for i in range(0, n):
    s = lsv[i]
    print((i + 1),"\t", s["Student ID"],"\t", s["Student name"], "\t","\t", s["Dob"])

crs = []
for i in range(0, m):
    print("Course : " +str(i + 1) )
    crsId = input("Course ID: ")
    crsName= input("Course name: ")
    c = {
        "Course name": crsName,
        "Course id" : crsId,
    }
    crs.append(c)
print("No \t Course ID \t Course name   ")
for i in range(0, m):
    x = crs[i]
    print((i + 1), "\t", x["Course id"], "\t", "\t", x["Course name"])
    
grd = []    
a = int(input("Select a course: " ))
for i in range(0,m):
    if i + 1 == a:
       
        for i in range(0,n):
            print("Information of student no " +str(i + 1))
            
            grade = input("Grade: ")
            z= {
                
               
                "grade" : grade,
            }
            grd.append(z)
    
print("Course \t N0 \t Student ID \t Student Name \t Grade ")
for i in range(0,n):
        y= grd[i]
        k= lsv[i]
        print(c["Course name"],"\t", (i + 1),"\t", k["Student ID"], "\t", k["Student name"], "\t", y["grade"] )