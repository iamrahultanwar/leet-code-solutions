class Solution:
    def climbStairs(self,n:int)->int:
        one,two = 1,1
        
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
            
        return one
#     def climbStairs(self, n: int) -> int:
#         currentNumberOfWays = 0
#         waysToTop = [1]

#         for currentHeight in range(1,n+1):
#             startOfWindow = currentHeight - 3
#             endOfWindow = currentHeight - 1

#             if startOfWindow >= 0:
#                 currentNumberOfWays -= waysToTop[startOfWindow]

#             currentNumberOfWays += waysToTop[endOfWindow]
#             waysToTop.append(currentNumberOfWays)

#         return waysToTop.pop()
        