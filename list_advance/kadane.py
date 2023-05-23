def kadane(nums: list[int]) -> int:
    """
    function that returns a maximum of a sub-array
    """
    sums = 0
    maxi = nums[0]
    for i in range(0, len(nums)):
        sums += nums[i]
        maxi = max(sums, maxi)
        if sums < 0:
            sums = 0
    return maxi
