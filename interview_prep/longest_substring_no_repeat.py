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

def longest_substring_init(s: str) -> int:
    longest_substringstring = 0
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

        longest_substringstring = max(longest_substringstring, current_substring_length)
    return longest_substringstring

    
def longest_substring(s: str) -> int:
    letter_map = {}
    left = 0
    right = 0
    curr_distance = 0
    longest_distance = 0
    
    while right < len(s):     
        if s[right] not in letter_map:
            letter_map[s[right]] = 0
            right += 1
            curr_distance += 1
            if curr_distance > longest_distance:
                longest_distance = curr_distance
        else:
            letter_map.pop(s[left])
            left += 1
            curr_distance -= 1
            
    return longest_distance


if __name__ == '__main__':
    assert longest_substring('abe') == 3, f"longest_substring('abe') == 3, found {longest_substring('abe')=}"
    assert longest_substring('abcabcbb') == 3, f"longest_substring('abcabcbb') == 3, found {longest_substring('abcabcbb')=}"
    assert longest_substring('bbbbb') == 1, f"longest_substring('bbbbb') == 1, found {longest_substring('bbbbb')=}"
    assert longest_substring('abcc') == 3, f"expected longest_substring('abcc') == 3, instead {longest_substring('abcc')=}"
    assert longest_substring('aabc') == 3, f"expected longest_substring('aabc') == 3, instead {longest_substring('aabc')=}"
    assert longest_substring('abcck') == 3, f"expected longest_substring('abcck') == 3, instead {longest_substring('abcck')=}"
    assert longest_substring('abczck') == 4, f"expected longest_substring('abczck') == 4, instead {longest_substring('abczck')=}"

    assert longest_substring('pwwkew') == 3, f"expected longest_substring('pwwkew') == 3, instead {longest_substring('pwwkew')=}"
    assert longest_substring('pwwwkp') ==  3, f"longest_substring('pwwwkp') == 3, found {longest_substring('pwwwkp')=}"

    assert longest_substring('contiguous') ==  7, f"longest_substring('contiguous') == 7, found {longest_substring('contiguous')=}"
    
    assert longest_substring('haagen-dazs') ==  8, f"longest_substring('haagen-dazs') == 9, found {longest_substring('haagen-dazs')=}"
    assert longest_substring('cnotiguous') ==  7, f"longest_substring('contiguous') == 7, found {longest_substring('contiguous')=}"
