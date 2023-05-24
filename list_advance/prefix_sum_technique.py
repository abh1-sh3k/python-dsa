def get_sum(p_sum: list[int], left: int, right: int) -> int:
    if left == 0:
        return p_sum[right]
    else:
        return p_sum[right] - p_sum[left - 1]


def prefix_sum_technique(arr: list[int], arr_range: list[int])->int:
    """
    returns sum of element in a given range(inclusive)
    """
    p_sum = [None] * len(arr)
    p_sum[0] = arr[0]
    #CUMMALTIVE FREQ
    for i in range(1, len(arr)):
        p_sum[i] = p_sum[i - 1] + arr[i]
    return get_sum(p_sum, arr_range[0], arr_range[1])
