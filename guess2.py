#2 3 4 5 6 7 8 9
'''
0 - 100
50
> 50
(100+50) / 2 => 75
> 75
(100+75) / 2 => 88
< 88
(75+88) / 2 => 
or
< 50
(0 + 50) / 2 => 25


50
l->0
h->100
m -> 50

if < m:
l->0 (unchanged)
h-> 50 (m)

if > m:
l-> m (50)
h->100(unchanged)


'''

low = 0
high = 100

# infinite loop
while(True):
    mid = int((low+high)/2)
    print('low: %d, high: %d, mid: %d' % (low, high, mid))
    guess = mid
    print(guess)
    print("Is the number correct, higher, or lower?")
    input_ = input('Enter: ')
    if input_ == "correct":
        print('Yay!')
        break
    elif input_ == "lower":
        high = mid
    elif input_ == "higher":
        low = mid
        
   


'''
low: 0, high: 100, mid: 50
50
Is the number correct, higher, or lower?
Enter: lower
low: 0, high: 50, mid: 25
25
Is the number correct, higher, or lower?
Enter: lower
low: 0, high: 25, mid: 12
12
Is the number correct, higher, or lower?
Enter: higher
low: 12, high: 25, mid: 18
18
Is the number correct, higher, or lower?
Enter: higher
low: 18, high: 25, mid: 21
21
Is the number correct, higher, or lower?
Enter: higher
low: 21, high: 25, mid: 23
23
Is the number correct, higher, or lower?
Enter: correct
Yay!
'''


#99, 76, 1, 5, 45
# next day: 31, 32















        
    
