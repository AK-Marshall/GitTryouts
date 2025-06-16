def findSmallest(oldArr):
    smallest=oldArr[0]
    smallest_index=0
    for i in range(1,len(oldArr)):
        if oldArr[i]<smallest:
            smallest=oldArr[i]
            smallest_index = i
    return smallest_index

def selectionSort(oldArr):
    newArr=[]
    for i in range(len(oldArr)):
        smallest=findSmallest(oldArr)
        newArr.append(oldArr.pop(smallest))
        
    return(newArr)

print(selectionSort([5,3,6,7,8,9,123123,123,3457,674,123]))

