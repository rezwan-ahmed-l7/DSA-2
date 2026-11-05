def LCS(S1, S2, i, j):

    if i == 0 or j == 0:
        return 0

    if S1[i - 1] == S2[j - 1]:
        return 1 + LCS(S1, S2, i - 1, j - 1)
    else:
        return max(LCS(S1, S2, i - 1, j), LCS(S1, S2, i, j - 1))


S1 = "ABCD"
S2 = "ACBD"
print("LCS length:", LCS(S1, S2, len(S1), len(S2)))
