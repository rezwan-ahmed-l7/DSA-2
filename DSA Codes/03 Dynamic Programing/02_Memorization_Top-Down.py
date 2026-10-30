n = 8
dp = [-1] * (n + 1)


def fib(num, dp):
    if num <= 1:
        return num
    if dp[num] != -1:
        return dp[num]
    dp[num] = fib(num - 1, dp) + fib(num - 2, dp)
    return dp[num]


print(fib(n, dp))
print(dp)
