# Binary Search

def binary_search(input_array, value):
    arr = input_array
    hi = len(arr)-1
    lo = 0
    while lo < hi:
        mid = (hi + lo) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] < value:
            lo = mid+1
        else:
            hi = mid
        
    if arr[lo] == value:
        return lo
    else:
        return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
