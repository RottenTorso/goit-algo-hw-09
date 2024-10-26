import time

def find_coins_greedy(amount):
    # Номінали монет
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    # Ітерація по номіналах монет
    for coin in coins:
        if amount >= coin:
            # Визначення кількості монет даного номіналу
            count = amount // coin
            amount -= count * coin
            result[coin] = count
    return result

def find_min_coins(amount):
    # Номінали монет
    coins = [50, 25, 10, 5, 2, 1]
    # Ініціалізація масиву для зберігання мінімальної кількості монет для кожної суми
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    # Масив для зберігання кількості монет для кожної суми
    coin_count = [0] * (amount + 1)
    # Масив для зберігання останньої використаної монети для кожної суми
    coin_used = [0] * (amount + 1)

    # Ітерація по всіх сумах від 1 до amount
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    result = {}
    # Відновлення результату за допомогою масиву coin_used
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result

def compare_algorithms(amount):
    # Вимірювання часу для жадібного алгоритму
    start = time.perf_counter()
    greedy_result = find_coins_greedy(amount)
    greedy_time = time.perf_counter() - start

    # Вимірювання часу для алгоритму динамічного програмування
    start = time.perf_counter()
    dp_result = find_min_coins(amount)
    dp_time = time.perf_counter() - start

    return greedy_result, greedy_time, dp_result, dp_time

amount = 113
greedy_result, greedy_time, dp_result, dp_time = compare_algorithms(amount)

print(f"Greedy Result: {greedy_result}, Time: {greedy_time}")
print(f"DP Result: {dp_result}, Time: {dp_time}")
