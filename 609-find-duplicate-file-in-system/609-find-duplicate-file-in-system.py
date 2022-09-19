class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        result = defaultdict(list)
        
        for path in paths:         
            infoList = path.split(" ")
            
            root = infoList[0]
            
            for idx in range(1,len(infoList)):
                file = infoList[idx]
                filePath,text = file.split("(")
                result[f'({text}'].append(f'{root}/{filePath}')
        r = []
        for ans in result.values():
            if len(ans) > 1:
                r.append(ans)
                
        return r