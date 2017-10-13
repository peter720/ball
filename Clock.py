'''
clock
hour, minutes, AM-PM

'''

class Clock:

    # instance variables
    hour = 0
    minute = 0
    am_pm = ''

    # init-> initialize the instance variables
    def __init__(self, hour=0, minute=0, am_pm=''):
        self.hour = hour
        self.minute = minute
        self.am_pm = am_pm.upper()

    def addMinutes(self, minutes):
        minutes = self.minute + minutes
        if minutes >= 60:
            self.hour = self.hour + 1
            minutes = minutes - 60
            
            if self.hour >= 12:
                if self.am_pm == 'AM':
                    self.am_pm = 'PM'
                else:
                   self.am_pm = 'AM' 
                
        self.minute = minutes
        

    # magic method __str__() gives the string representation of the objects
    def __str__(self):
        return '{}:{:02d} {}'.format(self.hour, self.minute, self.am_pm)

    def isEqualTo(self, other):
        if self.minute == other.minute and self.hour == other.hour and self.am_pm == other.am_pm:
            return True
        return False

    def __eq__(self, other):
        if self.minute == other.minute and self.hour == other.hour and self.am_pm == other.am_pm:
            return True
        return False


clk = Clock() # this will create a Clock type variable (object)
clk.hour = 8
clk.minute = 8
clk.am_pm = 'AM'

print(clk)

clk2 = Clock(11, 23, 'PM')
print(clk2)

clk2.addMinutes(40)
print(clk2) #12:03 AM

clk3 = clk2 
clk3.minute = 45

print(clk2)#12:03 AM
print(clk3)#12:45 AM

clk4 = Clock(9, 30, 'am')
clk5 = Clock(9, 30, 'AM')

'''
def check(clk1, clk2):
    if clk1.minute == clk2.minute and clk1.hour == clk2.hour and clk1.am_pm == clk2.am_pm:
        print('pass')


check(clk4, clk5)

if clk4.isEqualTo(clk5):
    print('equal')
else:
    print('Not equal')
'''

if clk4 == clk5:
    print('equal')
else:
    print('Not equal')
    
# HW - study the code
