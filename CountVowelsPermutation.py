class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [[0 for i in range(5)] for j in range(n)]
        
        #for a string of length i, the number of strings is equal to the number of vowels, which is i.
        for i in range(5):
            dp[0][i] = 1
            
        if n == 1:
            return 5
        elif n == 0:
            return 0
            
        #if we have a string of more than one character, we need to consider the cases. Here, I am simply adding the dp array the total characters that can follow each other
        #character, so a = 1, e = 2, i = 4, o = 2, u = 1
        for i in range(5):
            if i == 0:
                dp[1][i] = 1
            elif i == 1:
                dp[1][i] = 2
            elif i == 2:
                dp[1][i] = 4
            elif i == 3:
                dp[1][i] = 2
            else:
                dp[1][i] = 1

  #Since this is a dp array, we have already solved most of the solutions to the equation, what I am doing here is adding all the potential solutions going down the line
  #If we start with a, we know that it can be followed by e and all cases that follow e, so the last row of the "e" case. I will do this for all vowels
        for i in range(2, n):
            for j in range(5):
                if j == 0:
                    dp[i][j] += dp[i-1][1]
                elif j == 1:
                    dp[i][j] += dp[i-1][0]
                    dp[i][j] += dp[i-1][2]
                elif j == 2:
                    dp[i][j] += dp[i-1][0]
                    dp[i][j] += dp[i-1][1]
                    dp[i][j] += dp[i-1][3]
                    dp[i][j] += dp[i-1][4]
                elif j == 3:
                    dp[i][j] += dp[i-1][2]
                    dp[i][j] += dp[i-1][4]
                else:
                    dp[i][j] += dp[i-1][0]

  #The last thing to do is to return the sum of all vowel cases and mod by a large number to keep from overflowing.
        return sum(dp[n-1]) % ((10**9) + 7)
