class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero=nums.count(0)
        one=nums.count(1)
        two=nums.count(2)
        nums.clear()
        for i in range(zero):
            nums.append(0)
        for i in range(one):
            nums.append(1)
        for i in range(two):
            nums.append(2)
            
        
