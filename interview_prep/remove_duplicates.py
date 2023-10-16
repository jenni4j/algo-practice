from typing import List

def remove_duplicates(nums: List[int]) -> List[int]:

    dupes = {}
    res = []

    for i in nums:
        if i not in dupes.keys():
            dupes[i] = 1
            res.append(i)

    return res


if __name__ == '__main__':
    res = remove_duplicates([1,13,3,3,3,4])
    print(res)