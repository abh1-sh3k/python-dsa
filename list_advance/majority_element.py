def majority_element(arr: list[int]) -> int:
    """
    returns a majority element if present in an array.
    when element is present (n/2) times more in an array.
    return -1 if no majority element is present
    """
    arr_index = 0
    count = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[arr_index]:
            count += 1
        else:
            count -= 1
        if count == 0:
            arr_index = i
            count = 1
    new_count = 0
    for _, value in enumerate(arr):
        if value == arr[arr_index]:
            new_count += 1
    return arr[arr_index] if new_count > len(arr)//2 else -1
