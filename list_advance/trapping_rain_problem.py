def get_water(arr: list):
    """
    function returns, how much water we can collect between blocks
    """
    left_max = [0] * len(arr)
    right_max = [0] * len(arr)
    trapped_water = 0
    left_max[0] = arr[0]
    for i in range(1, len(arr)):
        left_max[i] = max(arr[i], left_max[i - 1])
    right_max[len(arr) - 1] = arr[len(arr) - 1]
    for j in range(len(arr) - 2, -1, -1):
        right_max[j] = max(arr[j], right_max[j + 1])
    for k in range(1, len(arr) - 1):
        trapped_water = trapped_water + (min(left_max[k], right_max[k]) - arr[k])
    return trapped_water
