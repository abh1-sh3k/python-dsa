def element_last_index(arr: list[int], x: int) -> int:
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            if mid == len(arr) - 1 or arr[mid] != arr[mid+1]:
                return mid
            else:
                low = mid + 1
    return -1
