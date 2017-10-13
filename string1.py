p = input("enter a text")
o = "abcdefghijklmnopqrstuvwxyz" 
#q = "bcdefghijklmnopqrstuvwxyza"
#encrytion
final = ""
for i in range(len(p)):
    j = o.find(p[i])
    if j == 0:
        final = final + "z"
    else:
        final = final + o[j-1]
#decryption
x = ""
for i in range(len(final)):
    j = o.find(final[i])
    if j == 25:
        x = x + "a"
    else:
        x = x + o[j+1]
        
        
print(final)
print(x)
q = ""
print(len(p))
for i in range(len(p)):
    q = q + p[len(p)-1-i]
print(q)
    
    
