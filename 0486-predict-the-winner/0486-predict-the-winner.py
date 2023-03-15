class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def predict_the_winner(l, r):
            if l == r:
                return nums[l]
            left = nums[l]- predict_the_winner(l+1, r)
            right = nums[r] - predict_the_winner(l, r-1)
            
            return max(left, right)
        
        return predict_the_winner(0, len(nums)-1) >= 0