from typing import List


def merge_sort(arr: List[int], start: int, end: int) -> None:
    """
        Recursively apply merge sort to a list when it has more than one element

        >>> m = [7, 4, 5, 9, 6]
        >>> merge_sort(m, 0, len(m))
        >>> m
        [4, 5, 6, 7, 9]
    """
    if end-start < 2:
        return

    mid = (start+end)//2
    merge_sort(arr, start, mid)
    merge_sort(arr, mid, end)
    merge(arr, start, mid, end)


def merge(arr: List[int], start: int, mid: int, end: int) -> None:
    # Check if the array is already sorted and does not need merging
    if arr[mid-1] <= arr[mid]:
        return

    temp = []
    i = start
    j = mid
    while (i < mid and j < end):
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    """
        Check if there are extra items in the first half of the 2 subarray
        to be merged and copy them to the end of the list
    """
    l = len(temp)
    while (i < mid):
        arr[start+l] = arr[i]
        i += 1
        l += 1

    t = 0

    while(t < len(temp)):
        arr[start+t] = temp[t]
        t = t + 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
