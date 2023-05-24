def equilibrium_point(arr: list[int]) -> bool:
    left_side_sum = 0
    right_side_sum = sum(arr)
    for i in range(len(arr)):
        right_side_sum -= arr[i]
        if right_side_sum == left_side_sum:
            return True
        left_side_sum += arr[i]
    return False
