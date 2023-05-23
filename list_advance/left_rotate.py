def left_rotate(l: list, d: int):
    """
    function that takes a list and rotates it from left by d places
    :param l:list to rotate
    :param d: how many places you want the list to rotate from left
    :return: new rotated list
    """
    n = len(l)
    reverse(l, 0, d - 1)
    reverse(l, d, n - 1)
    reverse(l, 0, n - 1)
    return l


def reverse(l: list, start_index: int, end_index: int):
    """
    reverse a list
    """
    while start_index < end_index:
        l[start_index], l[end_index] = l[end_index], l[start_index]
        start_index += 1
        end_index -= 1
