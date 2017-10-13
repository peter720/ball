'''
class: Student
'''
class Student:
    
    '''
    grade= ''
    name = ''
    id = '000000'
    age = 0
    score = 0
    '''
    def __init__(self, name='', id='000000', age=0, score=0, grade=''):
        self.grade = grade
        self.name = name
        self.id = id
        self.age = age
        self.score = score
        

    def __str__(self):
        return '{0:6s}'.format(self.name) +' '+ self.grade+' '+ self.id + ' '+ str(self.age)

    def setScore(self,score):
        self.score = score
        if self.score >= 90:
            self.grade = 'A'
        elif self.score >= 80:
            self.grade = 'B'
        elif self.score >= 70:
            self.grade = 'C'
        elif self.score >= 60:
            self.grade = 'D'
        else:
            self.grade = 'F'
    
    '''
    def score(self, grade):
        if self > 90:
            return 'A'
        if self > 80:
            return 'B'
        if self < 60:
            return 'F'
    '''
################
student1 = Student()
#student1.grade = 90
student1.name = 'bob'
student1.id = '1001859'
student1.age = 15

student2 = Student('Mike', '1001860', 15)

student3 = Student('Sara', '1001861', 15) #
############################


# at the end of semester
student1.setScore(78)
student2.setScore(90)
student3.setScore(85)

print(student1.grade)


#print(student1)
#print(student2)
#print(student3)
'''
 hw:
 1) add a property called score to your class
 2) add a method, called setScore(), have  a parameter score, which will set the property score
 3) based on the score, set the grade

 > 90 = A
 > 80 = B
 < 60 = F
'''
