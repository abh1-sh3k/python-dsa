def max_appearing_element(left: list[int], right: list[int]) -> int:
    n = len(left)
    freq = [0] * 101
    for i in range(n):
        freq[left[i]] += 1
        freq[right[i] + 1] -= 1
    for i in range(1, 100):
        freq[i] += freq[i - 1]
    return max(freq)
