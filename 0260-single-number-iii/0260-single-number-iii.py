class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        temp = 0
        for num in nums:
            # print(f'num= {bin(num)}, temp={bin(temp)}')
            temp = temp ^ num
        
        first = 0
        # print(f'temp {bin(temp)}') # 6
        while not temp & (1<<first):
            # print(f'first {bin(first)}')
            first += 1
            
        # print(f'First= {bin(first)}') # 1

        
        num1, num2 = 0, 0
        for num in nums:
            if num & (1<<first):
                num1 = num1 ^ num
                # print(f'num1= {bin(num1)}, first= {bin(first)}')
            else:
                num2 = num2 ^ num
                # print(f'num2= {bin(num2)}, num= {bin(num)}')

        return [num1, num2]