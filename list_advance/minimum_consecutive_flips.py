def minimum_consecutive_flips(arr: list[int]):
    """
    gives the minimum of number of group flips to make all array elements same.
    """
    print(arr)
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            if arr[i] != arr[0]:
                print(f"from {i} to ", end="")
            else:
                print(i - 1)
    if arr[len(arr) - 1] != arr[0]:
        print(len(arr) - 1)
