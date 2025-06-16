def binary_search(mylist, item):
    low = 0
    high = len(mylist) - 1
    count=0
    while low <= high:
        mid = (low + high) // 2
        guess = mylist[mid]
        
        if item == guess:
            return count
        elif guess > item:
            high = mid - 1
            count+=1 
        else:
            low = mid + 1
            count+=1
          
    return None

my_list = [1, 5, 7, 9, 11, 13]
print(binary_search(my_list, 3))