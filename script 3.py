p = input("Enter a word")
y = ""
for i in range(len(p)):
    w = ord(p[i])
    y = y + str(w) + " "
    
l = y.split(" ")
print(l)
k = ""
for i in range(len(l)-1):
    m = chr(int(l[i]))
    k = k + m

print(y)
print(k)
    

    
