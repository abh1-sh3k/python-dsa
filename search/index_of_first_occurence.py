def element_first_index(arr: list[int], x: int) -> int:
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high+low)//2
        if arr[mid]>x:
            high = mid - 1
        elif arr[mid]<x:
            low = mid+1
        else:
            if mid == 0 or arr[mid-1]!=arr[mid]:
                return mid
            else:
                high = mid - 1
    return -1
