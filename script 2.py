w = input("enter how much times you want this to run")
m = int(w)
for  i in range(m):
    y = input("enter a year: ")
    x = int(y)
    if x%4 == 0:
        print("Yes it is a leap year")
    else:
        print("No it isn't a leap year")
        
