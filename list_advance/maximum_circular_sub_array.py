from list_advance.kadane import kadane


def circular_sub_array_maximum(arr: list[int]) -> int:
    x = kadane(arr)
    y = 0
    for i in range(0, len(arr)):
        y += arr[i]
        arr[i] *= -1
    z = kadane(arr)
    return x if y + z == 0 else max(x, y + z)
