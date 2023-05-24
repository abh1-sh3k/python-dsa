def window_sliding(arr: list[int], k: int) -> int:
    """
    returns max sum between k interval given
    """
    current = 0
    for i in range(k):
        current += arr[i]
    result = current
    for j in range(k, len(arr)):
        current += arr[j] - arr[j - k]
        result = max(current, result)
    return result
