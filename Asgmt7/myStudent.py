# Ehsan *** Feb. 9, 2021 *** Team IV *** Assignment Day 7 - myStudent Module
#6

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
listIp = list()
course = str()
mark = int()
txtIp = str()
vSl = list()
courseMarks = dict()
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