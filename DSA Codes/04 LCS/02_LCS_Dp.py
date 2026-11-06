def LCS(S1, S2, i, j,dp):
    if i == 0 or j == 0:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    if S1[i - 1] == S2[j - 1]:
        dp[i][j] = 1 + LCS(S1, S2, i - 1, j - 1, dp)
    else:
        dp[i][j] = max(LCS(S1, S2, i - 1, j, dp), LCS(S1, S2, i, j - 1, dp))

    return dp[i][j]


S1 = "ABCD"
S2 = "ACBD"

row = len(S1) + 1
col = len(S2) + 1

dp = [[-1 for _ in range(col)] for _ in range(row)]
print("LCS length:", LCS(S1, S2, len(S1), len(S2), dp))