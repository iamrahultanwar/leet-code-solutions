Approach
​
1. idea is to get two subset, we will take total / 2, because if we can create 1 sub array with total / 2, then its sure that there will another sub array so that total is justified
2. take target == sum(nums), if target is odd return False, else target = target // 2
3. rest is same to get subsetSumToK