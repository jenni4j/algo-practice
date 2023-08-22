def longest_substring(s: str) -> int:
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


if __name__ == '__main__':
    res = longest_substring('pwwkew')
    print(res)

