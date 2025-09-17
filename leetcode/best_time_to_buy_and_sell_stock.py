# LeetCode Problem: Best Time to Buy and Sell Stock
# Difficulty: Easy
# Source: NeetCode 150
# Topics: Array, Dynamic Programming
# Solved on: 17 Sept 2025

def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit
