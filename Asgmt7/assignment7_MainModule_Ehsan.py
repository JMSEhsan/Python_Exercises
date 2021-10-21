#  Ehsan *** Feb. 9, 2021 *** Team IV *** Assignment Day 7 - MainModule

import myStudent as AuxMod

#3
SJn = AuxMod.Student("John", "Smith", "December 1, 2006", 10, 10023, {"Math":90, "Science":88, "Social":77, "LA":98 })
print("\nCreate a new student:", " Firstname:", SJn.fname, " Lastname:", SJn.lname, " DOB:", SJn.DOB, " Grade:", SJn.gradeLevel, " StudentID:", SJn.studentID, " Courses:", SJn.courseMarks)
#4
SJn.addCourseMark("PE", 99)
SJn.addCourseMark("Math", 94)
print("\nAdded for him: (PE, 99), (Math, 94)\n\n")

 #5
txt = "(For John) Fullname:  {}   Total:  {:.2f}    His Courses:  {}    age: {}"
print(txt.format( SJn.getFullName(), SJn.GetTotal(), SJn.GetCourses(), SJn.getAge()))
print("\n               *** End ***                          \n")
