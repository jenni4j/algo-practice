def longest_substring(s: str, k: int) -> int:
    l = 0
    res = 0
    letter_count = {}

    for r in range(len(s)):
        letter_count[s[r]] = 1 + letter_count.get(s[r], 0)
        # maxf = max(maxf, letter_count[s[r]])

        while (r - l + 1) - max(letter_count.values()) > k:
            letter_count[s[l]] -= 1
            l += 1

        res = max(res, r - l + 1)

    return res


if __name__ == '__main__':
    assert longest_substring('ABAB', 2) == 4, f"longest substring = 4, found {longest_substring('ABAB', 2)}"