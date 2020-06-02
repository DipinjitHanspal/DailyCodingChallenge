"""
    Given an array of integers, return a new array such that each element
    at index i of the new array is the product of all the numbers in the 
    original array except the one at i.

    For example, if our input was[1, 2, 3, 4, 5], the expected output would 
    be [120, 60, 40, 30, 24]. If our input was[3, 2, 1], the expected output
    would be[2, 3, 6].
"""


def main(arr: list) -> list:
    ls1 = [1 for i in range(len(arr))]
    ls2 = [1 for i in range(len(arr))]
    print(arr)
    for i in range(1, len(arr)):
        ls1[i] = ls1[i - 1] * arr[i - 1]
        ls2[-i - 1] = ls2[-i] * arr[-i]
    mst = []
    for i in range(len(ls1)):
        mst.append(ls1[i] * ls2[i])
    return mst


def tst():
    arr = [1, 2, 3, 4, 5]
    print(main(arr))
    arr2 = [3, 2, 1]
    print(main(arr2))


tst()
