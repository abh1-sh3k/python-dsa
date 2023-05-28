def binary_search_iterative(arr: list[int], n: int, x: int) -> int:
    """
    function return the element if it is in the array and
    if not present it returns -1
    To binary search to work the array should be sorted
    """
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return x
        elif arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
    return -1


def binary_search_recursive(arr: list[int], x: int, low: int, high: int) -> int:
    """
    recursive solution of binary search algorithm
    """
    if low > high:
        return -1
    mid = (low + high) // 2
    print(low, high,mid)
    if arr[mid] == x:
        return arr[mid]
    elif arr[mid] > x:
        return binary_search_recursive(arr, x, low, mid - 1)
    else:
        return binary_search_recursive(arr, x, mid + 1, high)
