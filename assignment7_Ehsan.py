print("\n\t\033[1;30;47m Ehsan *** Feb. 9, 2021 *** Team IV *** Assignment Day 7 \033[0;37;40m\n")

#1
class Person:
    def __init__(self, fname, lname, DOB):
        self.fname = fname
        self.lname = lname
        self.DOB = DOB

    def getFullName(self):
        txt = self.fname + " " + self.lname
        return txt

    def getAge(self):
        import datetime
        td = datetime.datetime.now()
        listDt = self.DOB.split(",")
        DOBYint = int(listDt[1])
        return int(td.strftime("%Y")) - DOBYint
#2


class Student(Person):
    def __init__(self, fname, lname, DOB, gradeLevel, studentID, courseMarks):
        super().__init__(fname, lname, DOB)
        self.gradeLevel = gradeLevel
        self.studentID = studentID
        self.courseMarks = courseMarks
    def addCourseMark(self, course, mark):
        dictIp = dict()
        listIp= (course, mark)
        dictIp.update({listIp[0].strip():int(listIp[1])})
        return self.courseMarks.update(dictIp)

    def GetTotal(self):
        import statistics
        vSl= [x for x in self.courseMarks.values()]
        return statistics.mean(vSl)
      
    def GetCourses(self):
        return [x for x in self.courseMarks.keys()]
#3
SJn = Student("John", "Smith", "December 1, 2006", 10, 10023, {"Math":90, "Science":88, "Social":77, "LA":98 })
print("\nCreated a new student:", "Firstname:", SJn.fname, " Lastname:", SJn.lname, " DOB:", SJn.DOB, " Grade:", SJn.gradeLevel, " StudentID:", SJn.studentID, " Courses:", SJn.courseMarks)
#4
SJn.addCourseMark("PE", 99)
SJn.addCourseMark("Math", 94)
print("\nAdded for him: (PE, 99), (Math, 94)\n\n")

 #5
txt = "(For John) Fullname:  {}   Total:  {:.2f}    His Courses:  {}    age: {}"
print(txt.format( SJn.getFullName(), SJn.GetTotal(), SJn.GetCourses(), SJn.getAge()))
print("\n               *** End ***                          \n")
