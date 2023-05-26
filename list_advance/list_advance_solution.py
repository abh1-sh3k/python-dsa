class Solutions:
    """
    List Advance Questions Solutions
    """

    def check_rotated_and_sorted(self, arr: list[int]) -> bool:
        """
        Given an array arr[] of N distinct integers, check if this array is Sorted (non-increasing or non-decreasing)
        and Rotated counter-clockwise.
        Check if array is sorted and rotated
        returns true if array is sorted otherwise false
        """
        # check non decreasing order
        count_inc = 0
        count_dec = 0
        for i in range(len(arr)):
            if arr[0] < arr[len(arr) - 1]:
                break
            if arr[i] > arr[(i + 1) % len(arr)]:
                count_inc += 1
        for i in range(len(arr)):
            if arr[0] > arr[len(arr) - 1]:
                break
            if arr[i] < arr[(i + 1) % len(arr)]:
                count_dec += 1
        if count_inc == 1 or count_dec == 1:
            return True
        return False

    def maximum_index(self, arr: list[int]) -> int:
        """
        Given an array A[] of N positive integers. The task is to find the maximum of j - i subjected to the constraint
        of A[i] < A[j] and i < j.
        returns maximum j-i from given array
        """
        left = [0] * len(arr)
        right = [0] * len(arr)
        # storing element smaller than current element arr[i] from its left
        left[0] = arr[0]
        for i in range(1, len(arr)):
            left[i] = min(arr[i], left[i - 1])
        # storing element greater than current element arr[i] from its right
        right[len(arr) - 1] = arr[len(arr) - 1]
        for j in range(len(arr) - 2, -1, -1):
            right[j] = max(arr[j], right[j + 1])
        # counter for left and right arrays
        i, j = 0, 0
        diff_max = -1
        while j < len(arr) and i < len(arr):
            if left[i] <= right[j]:
                diff_max = max(diff_max, j - i)
                j += 1
            else:
                i += 1
        return diff_max

    def stock_buy_and_sell(self, arr: list[int]) -> int:
        """
        alist = [[i,i+1] for i in range(n-1) if a[i]<a[i+1]]
        return alist
        """
        # code here
        alist = [[i, i + 1] for i in range(n - 1) if a[i] < a[i + 1]]
        return alist

    def trappingWater(self, arr: list[int], n: int) -> int:
        """
        function returns, how much water we can collect between blocks
        """
        left = [0] * n
        right = [0] * n

        left[0] = arr[0]
        for i in range(1, n):
            left[i] = max(arr[i], left[i - 1])

        right[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            right[i] = max(arr[i], right[i + 1])
        trapped_water = 0
        for i in range(1, n - 1):
            trapped_water = trapped_water + (min(right[i], left[i]) - arr[i])
        return trapped_water

    def maxEvenOdd(self, arr: list[int], n: int) -> int:
        """
        You are given an array of size n. Find the maximum possible length of a subarray such that its elements are
        arranged alternately either as even and odd or odd and even .
        """
        # returns: the maximum length
        max_count = 0
        count = 1
        for i in range(1,n):
            if arr[i] % 2 != arr[i - 1] % 2:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)
        return max_count
