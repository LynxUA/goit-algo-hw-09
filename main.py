import time

def find_coins_greedy(amount, denominations=[50, 25, 10, 5, 2, 1]):
    result = {}
    for coin in denominations:
        if amount >= coin:
            count = amount // coin
            amount -= coin * count
            result[coin] = count
    return result

def find_min_coins(amount, denominations=[50, 25, 10, 5, 2, 1]):
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    coin_combination = [None] * (amount + 1)
    
    for coin in denominations:
        for i in range(coin, amount + 1):
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_combination[i] = coin
    
    result = {}
    current_amount = amount
    while current_amount > 0:
        coin = coin_combination[current_amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current_amount -= coin
    
    return result

def compare_algorithms(amount):
    start_time = time.time()
    greedy_result = find_coins_greedy(amount)
    greedy_time = time.time() - start_time
    
    start_time = time.time()
    dp_result = find_min_coins(amount)
    dp_time = time.time() - start_time
    
    print(f"Greedy Algorithm: {greedy_result}, Time: {greedy_time:.6f} seconds")
    print(f"Dynamic Programming Algorithm: {dp_result}, Time: {dp_time:.6f} seconds")

compare_algorithms(113)
compare_algorithms(1000)
compare_algorithms(10000)