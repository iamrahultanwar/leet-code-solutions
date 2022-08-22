class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        # 1,1,2
        
        result = []
        
        def dfs(sub,counter):
            
            if len(sub) == len(nums):
                result.append(sub[::])
                return
            
            for num in counter:
                if counter[num] > 0:
                    sub.append(num)
                    counter[num] -= 1
                    dfs(sub,counter)
                    sub.pop()
                    counter[num] += 1
                
            
            
        dfs([],Counter(nums))
        
        return result