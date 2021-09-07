#Program to generate Pascal's triangle. Pascal's Triangle is an excersize in a lot of addition at once. Each column is a different set of numbers. The first column is a set of
#one's, that's it. The second column are the natural integers in order, i.e. 1,2,3,4,5... etc. The third column is the triangular set of numbers or, the natural numbers, in sequence,
#added together up to that point. This is what that looks like: 1,3 = 2+1, 6 = 3+2+1, 10 = 4+3+2+1, 15 = 5+4+3+2+1, etc. The fourth column is the set of tetrahedral numbers or
#the triangular numbers added together so 1, 4 = 3+1, 10 = 6+3+1, etc. Following this sequence, we can build a dynamic program which adds together the different columns
#up to that point in order to build the triangle.

numRows = 5
dp = [[0 for i in range(numRows)] for j in range(numRows)]

#This function will go through and actually build the triangle
def generateDP(numRows):
    dp[0][0] = 1
    for i in range(numRows):
        for j in range(i, numRows):
            if i == 0:  #the first number in the first column will be 1 since that is the first real integer
                dp[j][i] = 1
            elif i == j:  #The first non-zero number in each column that isn't the first will be one,
                dp[j][i] = 1
            else: #Otherwise, we have to look at this function in order to solve the correct array value.
                dp[j][i] = getSum(dp, i, j)
    return dp

#getSum simply gets the sum from the previous boxes or, it is building out the triangle. This will work for a theoretically infinite number of rows in Pascal's triangle
def getSum(dp, col, end):
    sum = 0
    for i in range(end):
        sum += dp[i][col-1]
    return sum

def generateOutput(dp, row):
    return dp[row][0:row+1]

output = []
dp = generateDP(numRows)
for i in range(numRows):
    output.append(generateOutput(dp, i))

print(output)
