import random

# Quick Sort 

def quicksort(array):
    qs(array, 0, len(array)-1)
    return array

def qs(array, left, right):
    if left >= right:
        return
    
    pivot = array[random.randint(left,right)]
    partition = partition_arr(array, left, right, pivot)
    qs(array, left, partition-1)
    qs(array, partition, right)

def partition_arr(array, left, right, pivot):
    
    while left <= right:
        
        while array[left] < pivot:
            left+=1
            
        while array[right] > pivot:
            right-=1
        
        if left <= right:
            temp = array[right]
            array[right] = array[left]
            array[left] = temp
            left+=1
            right-=1    
        
    return left     

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)