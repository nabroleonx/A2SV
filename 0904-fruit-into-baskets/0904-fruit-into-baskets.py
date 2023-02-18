class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hashMap = {}
        '''
        [1,2,3,2,2]      
        {2: 3, 3: 1}       
        [1,2,2,3,4]      
        {3:1, 4:}  
        [3,3,3,1,2,1,1,2,3,3,4] 
        '''
        
        res = 0
        l = 0
        
        for i in fruits:
            if len(hashMap.keys()) == 2 and i not in hashMap:
                print(f'at index {l} and element {i}')
                print("Fruit ", fruits[l])
                
                while len(hashMap.keys()) > 1:
                    hashMap[fruits[l]] -= 1
                    if hashMap[fruits[l]] == 0:
                        del hashMap[fruits[l]]
                    l += 1
                
                #if fruits[l] in hashMap:
                 #   del hashMap[fruits[l]]
                #l += 1
            hashMap[i] = hashMap.get(i, 0) + 1
            
            res = max(res, sum(hashMap.values()))
            
            print(hashMap)
        
        return res