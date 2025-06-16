def binary_search(list,item):
    low = 0
    high = len(list)-1
     
    while low<=high:
        mid = (low + high) // 2
        guess = list[mid]
        if item == guess: 
            return mid
        elif guess > item:
            high = mid - 1
        else:
            mid = mid + 1
    return None
            
            
my_list = [1,5,7,9,11,13]
print(binary_search(my_list,5))