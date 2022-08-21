Approach
​
1. loop over board row,col
2. check for empty position
3. check for valid value from 1 - 9 if valid backtrack
​
How to check valid position
​
1. loop over 0-9
2. check for row if same char is presend return False
3. check for col if same char is present return False
4. to check in the 3X3 board you need to apply this logi
5. `board[ 3 * (row //3) + (i//3)][3 * (col // 3) + i%3]`