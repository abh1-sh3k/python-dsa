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
        for i in range(1, n):
            if arr[i] % 2 != arr[i - 1] % 2:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)
        return max_count

    def kadane(self, nums: list[int]) -> int:
        """
        function that returns a maximum of a sub-array
        """
        sums = 0
        maxi = nums[0]
        for i in range(0, len(nums)):
            sums += nums[i]
            maxi = max(sums, maxi)
            if sums < 0:
                sums = 0
        return maxi

    def circularSubarraySum(self, arr: list[int], n: int) -> int:
        """
        Given an array arr[] of N integers arranged in a circular fashion.
        Your task is to find the maximum contiguous subarray sum.
        """
        x = self.kadane(arr)
        y = 0
        for i in range(n):
            y += arr[i]
            arr[i] *= -1
        z = self.kadane(arr)
        return x if y + z == 0 else max(x, y + z)

    def arrange(self, arr: list[int], n: int) -> list[int]:
        """
        Given an array arr[] of size N where every element is in the range from 0 to n-1.
        Rearrange the given array so that the transformed array arrT[i] becomes arr[arr[i]].
        """
        for i in range(n):
            x = arr[i]
            y = arr[x]
            arr[i] = x + (y % n) * n
            print(f"x:{x} y:{y}  arr[{i}]:{arr[i]}")
        for i in range(n):
            arr[i] //= n
        return arr

    def game(self, a: int, b: int) -> bool:
        if 0 in [a, b]:
            return False

        if a > b:
            t = a
            a = b
            b = t

        k = b - a
        d = 1 + 5 ** 0.5

        d = d / 2
        d = d * k

        c = int(d)
        print(f"c {c},d {d}, k {k}")
        # Return answer
        return 0 if a == c else 1

    def missingNumber(self, arr: list[int], n: int) -> int:
        """
        find smallest positive missing number from the given array
        """
        if len(arr) == 1:
            return 1
        i = 0
        while i < n:
            if 0 < arr[i] <= n and arr[arr[i] - 1] != arr[i]:
                arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
            else:
                i += 1
        for i in range(n):
            if i + 1 != arr[i]:
                return i + 1
        return n + 1

    def div_and_subt(self, N: int):
        if N == 1:
            return "Arya"
        if N < 6:
            return "Jon"

        # make a dp array of size N+1
        arr = [0] * (N + 1)

        # Initialize the variable
        i = 1

        # If it's whose turn it is to win on that move, we'll do 1, otherwise 0

        # for 1-5 Jon always win
        while i < 6 and i <= N:
            arr[i] = 1
            i += 1

        i = 6
        while i <= N:
            # Whosever turn will it be we will
            # check if there is any move by
            # performing, there is a chance for
            # him to win, means if any
            # arr[condition] = 0 then he will win
            # for sure else not
            if arr[i // 2] == 0 or arr[i // 4] == 0 or arr[i // 3] == 0 or arr[i // 5] == 0:
                # Means the person doing the move can win through division
                arr[i] = 1
            elif arr[i - 2] == 0 or arr[i - 3] == 0 or arr[i - 4] == 0 or arr[i - 5] == 0:
                # Means the person doing the move can win through subtraction
                arr[i] = 1
            else:
                # Else other person will win
                arr[i] = 0
            print(arr)
            i += 1

        # If arr[N] is 1 then Jon win else Arya win
        return "Jon" if (arr[N] == 1) else "Arya"
