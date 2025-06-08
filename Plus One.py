class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit=[]
        get=''
        for i in digits:
            get+=str(i)
        get=int(get)+1
        for i in str(get):
            digit.append(int(i))
        return digit
