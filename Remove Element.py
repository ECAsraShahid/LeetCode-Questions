class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        while True:
            try:
                if nums[i] ==val:
                    nums.remove(nums[i])    
                else:
                    i+=1
            except IndexError:
                break
        return len(nums)
