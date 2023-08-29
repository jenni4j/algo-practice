from typing import List

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a: List[int], b: List[int]) -> List[int]:
    alice_points = 0
    bob_points = 0

    for i in range(len(a)):
        if a[i] < b[i]:
            bob_points += 1
        elif a[i] > b[i]:
            alice_points += 1

    return [alice_points, bob_points]

if __name__ == '__main__':
    res = compareTriplets([1,2,3], [4,5,6])
    print(res)