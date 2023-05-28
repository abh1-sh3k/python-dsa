from search.index_of_first_occurence import element_first_index
from search.index_of_last_occurence import element_last_index


def count(arr: list[int], x):
    """
    count the number of times an element has occurred
    """
    first_occurrence_index = element_first_index(arr, x)
    if first_occurrence_index == -1:
        return 0
    else:
        return element_last_index(arr, x) - first_occurrence_index + 1
