from typing import List

# abba: a a, b b, ab ba, abb bba

# 2 ifailuhkqq kkkk || 3 10 -> k k: 0 1, 1 2, 2 3, 0 2, 0 3, 1 3 | kk kk: 

# kkk || k k: 0 1, 1 2, 0 2 | kk kk: 01 12 

def anagram_pairs(k: int, strings: List[str]) -> List[int]:
    result = [0] * len(strings)
    for a, s in enumerate(strings):
        s_map = {}
        for i in range(len(s)):
            for j in range(i,len(s)):
                curr_substring = ''.join(sorted(s[i:j+1]))
                if s_map.get(curr_substring) is None:
                    s_map[curr_substring] = 1
                else:
                    s_map[curr_substring] += 1
        print(s_map)
        res = 0
        for item in s_map:
            c = s_map[item]
            # https://www.reddit.com/r/learnmath/comments/3bg21t/what_exactly_is_n_choose_2_in_probability/
            res += (c * (c - 1)) // 2
    
        result[a] = res

    return result
                

if __name__ == '__main__':
    res = anagram_pairs(1, ['kkk'])
    print(res)


