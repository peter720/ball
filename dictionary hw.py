



b = {
    'John Chan': '12/13/2003',
    'Siddharth Sundar Ramen': '12/13/2003',
    'Jonathan Choi': '3/29/2003',
    'Aneesh Saba': '08/15/2003',}

if 'Peter' in b: 
    print(b['Peter'])

print('Choose one of these people\'s birthdays: John Chan, Siddharth Sundar Ramen, Jonathan Choi, or Aneesh Saba')

print('Which one\'s birthday do you want to look up?')
name = input()
if name in b:
    print('{}\'s birthday is {}.'.format(name, b[name]))
else:
    print('Sadly, we don\'t have {}\'s birthday.'.format(name))

print('Enter a date: ')
birthday = input()

# http://collabedit.com/ehrf5

list = b.items()
found = 0
for key_value_pair in list:
    if key_value_pair[1] == birthday:
        print(key_value_pair[0]) # will print the name for matching birthdays
        found = 1
        
if found == 0:
    print('Sorry, try again!')

# list -> [(name, '12/13/2003'), (name2, '12/13/2003'), (name3, '3/29/2003'), (name4, '08/15/2003')] <- 
#                  0                       1                     2                       3
# list[0] -> (name, '12/13/2003')
# list[1] -> (name2, b)


# list2 = [[1,2], [3,4]] <====== list2
#            0      1

# list2[0] -> [1,2],  <-
# list2[0][0] -> 1
# list2[0][1] -> 2
# list2[1] -> [3,4]
# list2[1][0] -> 3
# list2[1][1] -> 4
