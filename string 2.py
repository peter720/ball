from random import randint

p = input("enter a text")
o = "abcdefghijklmnopqrstuvwxyz"
#
#'a', 'b' ,'c' .. 'z' #qazwsxedcrfvtgbyhnujmikolp
# i = 0, k = 2
# temp = q[2] -> temp = 'c'
# q[2] = q[0] -> 'a', 'b', 'a'
# q[0] = temp -> 'c', 'b', 'a'
# var = 6 
# 'c', 'b', 'a'
q = []
for i in range(len(o)):
    q.append(o[i])

#randomization of q
#15 <-> a
#randint(0,26) -> random indices / locations / positions
for i in range(52):
    k = randint(0,25)
    j = randint(0,25)
    temp = q[j]
    q[j] = q[k]
    q[k] = temp

encr = ""
for i in range(len(p)):
    index = ord(p[i]) - 97
    encr = encr + q[index]

print(encr)
decr = ""
for i in range(len(encr)):
    index = q.index(encr[i])
    ch = chr(index + 97)
    decr = decr + str(ch)

print(decr)






