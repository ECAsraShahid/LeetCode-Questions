class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedarray=[]
        mergedarray.extend(nums1)
        mergedarray.extend(nums2)
        
        length=len(mergedarray)
        mergedarray.sort()
        print("List arranged in ascending order:",mergedarray)
        if length%2!=0:
            x=int((length+1)/2)
            mid=mergedarray[x-1]
            return mid
        else:
            x=int(length/2)
            y=int((length+1)/2)
            mid=float((mergedarray[x-1]+mergedarray[y])/2)
            return mid
            
