Approach
​
1. Recursion
- we will go bottom to up
- return up + left
- base case will be to return 1 and 0
​
2. Memo # solution works here
- prepare a 2d array of len mXn
- check for value and store it in the 2d array
- return the last value in the array
​
3. Tabu
- prepare a 2d array and store 1 in `dp[0][0] = 1` for base case
- loop over this array and calculate up and left value if i > 0 and j > 0
- return last value in 2d array