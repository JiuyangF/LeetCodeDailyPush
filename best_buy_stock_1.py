"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""


def best_buy_sell_stock(price_list):
    best_buy = 0
    for i in range(len(price_list)):
        for j in range(len(price_list)):
            best_buy = max(price_list[j] - price_list[i], best_buy)
    print(best_buy)


def best_buy_sell_stock_2(prices):
    best_buy = 0
    for i in range(len(prices)):
        best_buy = max(max(prices[i::]) - prices[i], best_buy)
    return best_buy


def best_buy_sell_stock_3(prices):
    if not prices:
        return 0
    best_buy = 0
    min_price = prices[0]
    for i in range(len(prices)):
        if prices[i] < min_price:  # 获取前半段list中的最小值
            min_price = prices[i]
        else:
            # 用当前值减去前半段中的最小值，和已有的最优解进行比较，得出当前位置的最优解
            best_buy = max(prices[i] - min_price, best_buy)
    print(best_buy)


if __name__ == '__main__':
    price = [7, 1, 5, 3, 6, 4]
    # price = [1,2]
    # price = [1]
    # price = []
    best_buy_sell_stock(price)
