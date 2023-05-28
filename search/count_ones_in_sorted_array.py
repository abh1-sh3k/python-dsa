from search.index_of_first_occurence import element_first_index


def count_one(arr: list[int]) -> int:
    """
    count the number of occurence of 1s in an sorted array
    """
    first_index = element_first_index(arr, 1)
    return len(arr) - first_index if first_index != -1 else -1
