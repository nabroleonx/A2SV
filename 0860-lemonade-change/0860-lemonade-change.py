class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        no_five = 0
        no_ten = 0
        no_twenty = 0
        
        for bill in bills:
            if bill == 5:
                no_five += 1
            
            elif bill == 10:
                if no_five > 0:
                    no_five -= 1
                else:
                    return False
                no_ten += 1
            
            elif bill == 20:
                if no_five > 0 and no_ten > 0:
                    no_five -= 1
                    no_ten -= 1
                elif no_five >= 3:
                    no_five -= 3
                else:
                    return False
                no_twenty += 1
        
        return True