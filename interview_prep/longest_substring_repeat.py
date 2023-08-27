def longest_substring(s: str, k: int) -> int:
    left = 0
    right = 1
    longest_distance = 1
    curr_distance = 1
    curr_letter = s[left]
    temp_k = k
    temp_s = s
    
    while right < len(s):
        if temp_s[right] == curr_letter:
            curr_distance += 1
            if curr_distance > longest_distance:
                longest_distance = curr_distance 
            right += 1
        else:
            if temp_k == 0:
                temp_k = k
                temp_s = s
                left += 1
                curr_letter = temp_s[left]
                curr_distance -= 1
            else:
                temp_s[right] = curr_letter
                temp_k -= 1
                curr_distance += 1
                if curr_distance > longest_distance:
                    longest_distance = curr_distance
                right += 1
        
    return longest_distance

if __name__ == '__main__':
    assert longest_substring('AAB', 1) == 3, f"longest substring = 3, found {longest_substring('AAB', 1)}"