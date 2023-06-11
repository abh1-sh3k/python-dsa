class Sorting:
    """
    different sorting methods.
    Takes an array as input
    """
    res = 0

    def __init__(self, arr: list[int]):
        """
        initialize an array
        """
        self.arr = arr

    def __repr__(self):
        return f"Array -> {self.arr}"

    def bubble_sort(self):
        """
        STABLE SORT
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

    def selection_sort(self):
        """
        NOT STABLE
        Basic Idea is to find the minimum element and put it in the first position and so on.
        """
        n = len(self.arr)
        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                if self.arr[min_index] > self.arr[j]:
                    min_index = j
            self.arr[min_index], self.arr[i] = self.arr[i], self.arr[min_index]

    def insertion_sort(self):
        """
        STABLE
        Treat First element as sorted and right of it unsorted
        ---------------------
           SORTED | UNSORTED
        ---------------------
        0       i-1,i     n-1
        """
        n = len(self.arr)
        for i in range(1, n):
            element = self.arr[i]
            j = i - 1
            while j >= 0 and element < self.arr[j]:
                self.arr[j + 1] = self.arr[j]
                j -= 1
            self.arr[j + 1] = element

    def merge_sort(self, left: int, right: int):
        """
        STABLE ALGORITHM
        Divide, conquer and merge
        """
        if left < right:
            mid = (left + right) // 2
            self.merge_sort(left, mid)
            self.merge_sort(mid + 1, right)
            self.merge(left, mid, right)

    def merge(self, low, mid, high):
        left = self.arr[low:mid + 1]
        right = self.arr[mid + 1:high + 1]
        i, j = 0, 0
        k = low
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                self.arr[k] = left[i]
                i += 1
                k += 1
            else:
                self.arr[k] = right[j]
                j += 1
                k += 1
        while i < len(left):
            self.arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            self.arr[k] = right[j]
            j += 1
            k += 1

    @staticmethod
    def union(a: list[int], b: list[int]):
        """
        union of two sorted list
        prints non duplicated list
        :param a: sorted list
        :param b: sorted list
        """
        i, j = 0, 0
        while i < len(a) and j < len(b):
            if i > 0 and a[i] == a[i - 1]:
                i += 1
            elif j > 0 and b[j] == b[j - 1]:
                j += 1
            elif a[i] > b[j]:
                print(b[j], end=" ")
                j += 1
            elif a[i] < b[j]:
                print(a[i], end=" ")
                i += 1
            else:
                print(a[i], end=" ")
                i += 1
                j += 1
        while i < len(a):
            if i >= 0 and a[i] != a[i - 1]:
                print(a[i], end=" ")
                i += 1
        while j < len(b):
            if j >= 0 and b[j] != b[j - 1]:
                print(b[j], end=" ")
                j += 1
        print()

    @staticmethod
    def intersection(a: list[int], b: list[int]):
        """
        intersection of two sorted arrays
        returns same non duplicated arrays in ascending order
        """
        i, j = 0, 0
        while i < len(a) and j < len(b):
            if a[i] == a[i - 1] and i > 0:
                i += 1
                continue
            elif a[i] < b[j]:
                i += 1
            elif a[i] > b[j]:
                j += 1
            else:
                print(a[i], end=" ")
                i += 1
                j += 1

    def count_inv(self, left: int, right: int):
        """
        Where two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
        """
        res = 0
        if left < right:
            mid = (left + right) // 2
            res += self.count_inv(left, mid)
            res += self.count_inv(mid + 1, right)
            res += self.count_inv_merge(left, mid, right)
        return res

    def count_inv_merge(self, low, mid, high):
        i, j, k = 0, 0, low
        left = self.arr[low:mid + 1]
        right = self.arr[mid + 1:high + 1]
        res = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                self.arr[k] = left[i]
                i += 1
            elif left[i] > right[j]:
                self.arr[k] = right[j]
                res += len(left) - i
                j += 1
            k += 1
        while i < len(left):
            self.arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            self.arr[k] = right[j]
            k += 1
            j += 1
        return res

    def lomuto(self, low, high):
        """
        takes first element as a pivot
        pivot is returned.
        we know pivot will get placed at it's correct position
        """
        pivot = self.arr[high]
        i = low - 1
        for j in range(len(self.arr)):
            if self.arr[j] < pivot:
                i += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        self.arr[i + 1], self.arr[high] = self.arr[high], self.arr[i + 1]
        return i + 1
