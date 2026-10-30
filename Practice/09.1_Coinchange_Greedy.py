def coin_change_greedy(coins, amount):
    coins.sort(reverse=True)

    def backtrack(index, current_amount, count):
        if current_amount == 0:
            return count
        if index == len(coins):
            return float("inf")

        max_coins = current_amount // coins[index]
        min_total = float("inf")

        for x in range(max_coins, -1, -1):
            current_count = count + x
            if current_count >= min_total:
                break

            res = backtrack(index + 1, current_amount - x * coins[index], current_count)
            min_total = min(min_total, res)

        return min_total

    ans = backtrack(0, amount, 0)
    return ans if ans != float("inf") else -1


coins = [1, 2, 5]
amount = 11
print(coin_change_greedy(coins, amount))
