Approach
​
1. create counters
2. remove duplicates and sort the nums
3. loop over nums
1. calculate currEarn = nums[i] * counter[nums[i]]
2. check if curr numveb is adjacent or not
3. if yes calculate the max(currVal+prev,curr)
4. else currVal + cur