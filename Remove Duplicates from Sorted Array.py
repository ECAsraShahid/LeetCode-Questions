class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        store=nums[0]
        i=0
        j=1
        while i<len(nums):
            if nums[i]==store:
                i+=1
            else:
                nums[j]=nums[i]
                store=nums[i]
                i+=1
                j+=1
        return j
                
