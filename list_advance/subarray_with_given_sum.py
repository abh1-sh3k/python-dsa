def sub_array_with_given_sum(arr: list[int], given_sum: int) -> bool:
    """
    return true if given sum is present in sub array
    """
    start_point = 0
    current = 0
    for i in range(len(arr)):
        current += arr[i]
        while given_sum < current:
            current -= arr[start_point]
            start_point += 1
        if current == given_sum:
            return True
    return False
