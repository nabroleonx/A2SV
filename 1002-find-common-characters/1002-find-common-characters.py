class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res=[]
        
        for letter in words[0]:
            count=1
            
            for j in range(1,len(words)):
                if letter in words[j]:
                    count+=1
                    words[j]=words[j].replace(letter,"",1)     
            
            if count==len(words): 
                res.append(letter)
                
        return res
    