# [2 4 1 6 7 2 1 3
# [2 4 1 6 7 3]
def removeDuplicates(l):
    newList = []
    for i in range(len(l)):
        if l[i] not in newList:
            newList.append(l[i])
    return newList

print(removeDuplicates([2, 4, 1, 6, 7, 2, 1, 3]))
huisawesome72@gmail.com
