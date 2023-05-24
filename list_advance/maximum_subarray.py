def max_subarray(arr: list[int]) -> int:
    """
    returns maximum from a sub array
    """
    # using kadane's algorithm
    sum = 0
    maxi = arr[0]
    for i in range(0, len(arr)):
        sum += arr[i]
        maxi = max(maxi, sum)
        if sum < 0:
            sum = 0
    return maxi
