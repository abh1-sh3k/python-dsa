class Sorting:
    """
    different sorting methods.
    Takes an array as input
    """

    def __init__(self, arr:list[int]):
        """
        initialize an array
        """
        self.arr = arr

    def __repr__(self):
        return f"Array -> {self.arr}"

    def bubble_sort(self):
        """
        implementation of bubble sort algorithm
        basically we are shifting largest element to the last at each pass
        """
        n = len(self.arr)
        for i in range(n - 1):
            is_swapped = False
            for j in range(n - i - 1):
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
            if not is_swapped:
                return
