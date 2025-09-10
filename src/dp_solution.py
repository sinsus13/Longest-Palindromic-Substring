class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if n == 0 :
            return ''

        longest = 1
        begin = 0
        dp = [[False for _ in range(n)]for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if s[i] == s[j]:
                    if j - i == 1 or dp[i+1][j-1]:
                        dp[i][j] = True
                        if j - i + 1 > longest:
                            longest = j - i + 1
                            begin = i
        return s[begin:begin+longest]

