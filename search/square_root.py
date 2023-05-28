def square_root(x: int) -> int:
    """
    returns the math.floor(square root of x)
    """
    low = 1
    high = x
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            low = mid + 1
            ans = mid
        else:
            high = mid - 1
    return ans
