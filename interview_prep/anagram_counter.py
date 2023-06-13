# input: 2 strings
# output: 1 integer
# c c c / d d => delete e and f, integer = 2

def anagram_counter(string_one, string_two):
    string_one_map = {}
    string_two_map = {}
    count = 0

    for m in string_one:
        if m in string_one_map:
            string_one_map[m] += 1
        else:
            string_one_map[m] = 1
    
    for n in string_two:
        if n in string_two_map:
            string_two_map[n] += 1
        else:
            string_two_map[n] = 1
    
    for k in set(string_one_map.keys() + string_two_map.keys()):
        if k not in string_one_map and k in string_two_map:
            count += string_two_map[k]
        elif k not in string_two_map and k in string_one_map:
            count += string_one_map[k]
        else:
            count += abs(string_one_map[k] - string_two_map[k])
        
    return count


if __name__ == "__main__":
    res = anagram_counter("fcrxzwscanmligyxyvym", "jxwtrhvujlmrpdoqbisbwhmgpmeoke")
    print(res)


