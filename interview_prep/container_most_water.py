from typing import List

def container_max_brute(height: List[int]) -> int:
    max_area = 0
    for i in range(0, len(height) - 1):
        for j in range(i + 1, len(height)):
            left = i
            right = j 
            if height[left] <= height[right]:
                max_height = height[left]
            else:
                max_height = height[right]
            width = j - i
            curr_area = max_height * width
            if  curr_area > max_area:
                max_area = curr_area

    return max_area

def container_max(height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        container_height = min(height[left], height[right])
        curr_area = (right - left) * container_height
        max_area = max(max_area, curr_area)
        
        if height[left] >= height[right]:
            right -= 1
        else:
            left += 1
        
    return max_area




if __name__ == '__main__':
    res = container_max([1,8,6,2,5,4,8,3,7])
    print(res)