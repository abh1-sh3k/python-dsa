def max_profit_naive_solution(stock: list, start_index: int, end_index: int):
    """
    functions returns the max profit from buying and selling of stock
    Naive Solution
    """
    if start_index >= end_index:
        return 0
    total_profit = 0
    for i in range(start_index, end_index):
        for j in range(i + 1, end_index + 1):
            if stock[j] > stock[i]:
                curr_profit = stock[j] - stock[i] + \
                              max_profit_naive_solution(stock, 0, i - 1) + \
                              max_profit_naive_solution(stock, j + 1, end_index)
                total_profit = max(total_profit, curr_profit)
    return total_profit


def max_profit(stock: list):
    """
    functions returns the max profit from buying and selling of stock
    Cumulative Profit
    Efficient Solution
    """
    profit = 0
    for i in range(1, len(stock)):
        if stock[i] > stock[i - 1]:
            profit += stock[i] - stock[i - 1]
    return profit
