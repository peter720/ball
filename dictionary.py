dict = {'Peter':20, 'Aditi':23}
'''
 key : value
 keys -> 'Peter', 'Aditi'
 values -> 13, 23

[2, 3, 6, 8, 1]
 0  1  2  3  4

 dict['Peter'] -> 13
 dict['Aditi'] -> 23

 dict['Peter'] = 16
 dict['Peter'] = 20

[2 4 1 6 7 2 1 3 4 5 67 34 2 1 8 7 9 6]

'''

c = [2, 4, 1, 6, 7, 2, 1, 3, 4, 5, 67, 34, 2, 1, 8, 7, 9, 6]
d = {}
count = 0
# element : number of duplicates
# 2 : 3 <- key-value pair
# 4 : 2
# 1 : 3
# ...
# {2:3, 4:2, 1:3, 6:2, 7:2, 3:1, 5:1, 67:1, 34:1, 8:1, 9:1}
# 1 loop
for i in range(len(c)):
    if c[i] in d:
        d[c[i]] = d[c[i]] + 1
    else:
        d[c[i]] = 1
               
'''
for i in range(len(c)):
    #dict[key] = value
    
    if c[i] not in d:
        d[c[i]] =c.count(c[i])
'''
print(d)
    
