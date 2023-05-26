class Solutions:
    """
    List Advance Questions Solutions
    """

    def check_rotated_and_sorted(self, arr: list[int]) -> bool:
        """
        Given an array arr[] of N distinct integers, check if this array is Sorted (non-increasing or non-decreasing) and
        Rotated counter-clockwise.
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
