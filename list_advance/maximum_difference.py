def list_max_difference(l: list):
    """
    function that return a maximum difference between
    two element in a list.
    Note: l[j]-l[i] and i<j
    returns a None if a list is empty or max difference value if list not empty
    """
    if l is []:
        return None
    result = l[1] - l[0]
    min_val = l[0]
    for j in range(1, len(l)):
        result = max(result, l[j] - min_val)
        min_val = min(min_val, l[j])
    return result
