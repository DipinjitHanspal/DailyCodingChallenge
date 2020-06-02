"""
    Given an array of integers, return a new array such that each element
    at index i of the new array is the product of all the numbers in the 
    original array except the one at i.

    For example, if our input was[1, 2, 3, 4, 5], the expected output would 
    be [120, 60, 40, 30, 24]. If our input was[3, 2, 1], the expected output
    would be[2, 3, 6].
"""


def main(arr: list) -> list:
    ##
    # Solution : Construct 2 arrays, starting from opposite ends of the input arr
    # for which each successive element is a product of the previous time the current in the arr
    # For example, if the input array is [1, 2, 3], then ls1 = [1, 1*a[0], 1*a[0]*a[1]], ls2 = [1, 1*a[2], 1*a[2]*a[1]]
    # Now, between ls1 and ls2, you have every combination of multiplcation between the elements of the array. If you want
    # to find the value at arr[1], you multiply every value except arr[1], so you take ls1[1] * ls2[1]. If you reverse ls2 to
    # [1*a[2]*a[3], 1*a[2], 1], then you can do an element-wise multitplicaiton with ls1 such that
    # output = [1 * 1 * a[2] * a[3], 1*a[0]*1*a[2], 1*a[0]*a[1]*1]. Thus, this produces the desired output,
    # without division, in O(n) time and O(n) space.
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
