class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        res = []
        binary = [0,1]
        self.generate(res, "", binary, n)
        return [int(num, 2) for num in res] # convert int to binary
    
    def generate(self, res, path, binary, target_len):

        if len(path) == target_len:
            res.append(path[:])
            return
        
        for i in range(0, 2):
            path += str(binary[i])
            if binary[i] == 0:
                self.generate(res, path, binary, target_len)
            else:
                binary[0], binary[1] = binary[1], binary[0]
                self.generate(res, path, binary, target_len)
                binary[0], binary[1] = binary[1], binary[0]
            path = path[:-1]