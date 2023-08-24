def longest_substring_brute(s: str) -> int:
    max_length = 0
    for i, a in enumerate(s):
        curr_string = {}
        curr_string[a] = 1
        curr_length = len(curr_string.keys())
        if max_length < curr_length:
            max_length = curr_length
        for b in s[i + 1:]:
            if curr_string.get(b) is None:
                curr_string[b] = 1
                curr_length = len(curr_string.keys())
                if max_length < curr_length:
                    max_length = curr_length
            else:
                curr_string = {}
                continue

    return max_length

def longest_substring(s: str) -> int:
    max_length = 0 
    left = 0
    right = len(s) - 1
    left_map = {}
    right_map = {}

    while left <= right:
        if left_map.get(s[left]) is None and right_map.get(s[right]) is None:
            if left == right:
                left_map[s[left]] = left
                left += 1
            else:
                left_map[s[left]] = left
                right_map[s[right]] = right
                left += 1
                right -= 1
        else:
            break
    

    return max_length

def longest_sub(s: str) -> int:
    longest_substring = 0
    current_substring_length = 0
    some_map = {}

    for i, letter in enumerate(s):
        if letter not in some_map:
            some_map[letter] = i
            current_substring_length += 1
        else:
            length_to_previous_letter_occurence = i - some_map[letter]
            crosses_double_letter_boundary = length_to_previous_letter_occurence > current_substring_length
            if crosses_double_letter_boundary:
                current_substring_length += 1
            else:
                current_substring_length = length_to_previous_letter_occurence
            some_map[letter] = i

        longest_substring = max(longest_substring, current_substring_length)
    return longest_substring

    
def longest_sub(s: str) -> int:
    letter_bank = {}
    left = 0
    right = 0
    curr_distance = 0
    longest_distance = 0
    

    while right < len(s):     
        if letter_bank.get(s[right]) != 1:
            letter_bank[s[right]] = 1
            right += 1
            curr_distance += 1
            if longest_distance < curr_distance:
                longest_distance = curr_distance
            
        else:
            #abca
            letter_bank[s[left]] = 0
            left += 1
            curr_distance -= 1
            

    return longest_distance


if __name__ == '__main__':
    assert longest_sub('abe') == 3, f"longest_sub('abe') == 3, found {longest_sub('abe')=}"
    assert longest_sub('abcabcbb') == 3, f"longest_sub('abcabcbb') == 3, found {longest_sub('abcabcbb')=}"
    assert longest_sub('bbbbb') == 1, f"longest_sub('bbbbb') == 1, found {longest_sub('bbbbb')=}"
    assert longest_sub('abcc') == 3, f"expected longest_sub('abcc') == 3, instead {longest_sub('abcc')=}"
    assert longest_sub('aabc') == 3, f"expected longest_sub('aabc') == 3, instead {longest_sub('aabc')=}"
    assert longest_sub('abcck') == 3, f"expected longest_sub('abcck') == 3, instead {longest_sub('abcck')=}"
    assert longest_sub('abczck') == 4, f"expected longest_sub('abczck') == 4, instead {longest_sub('abczck')=}"

    assert longest_sub('pwwkew') == 3, f"expected longest_sub('pwwkew') == 3, instead {longest_sub('pwwkew')=}"
    assert longest_sub('pwwwkp') ==  3, f"longest_sub('pwwwkp') == 3, found {longest_sub('pwwwkp')=}"

    assert longest_sub('contiguous') ==  7, f"longest_sub('contiguous') == 7, found {longest_sub('contiguous')=}"
    
    assert longest_sub('haagen-dazs') ==  9, f"longest_sub('haagen-dazs') == 9, found {longest_sub('haagen-dazs')=}"
    assert longest_sub('cnotiguous') ==  7, f"longest_sub('contiguous') == 7, found {longest_sub('contiguous')=}"
