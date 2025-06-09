class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        value=0
        lst1=[]
        lst2=[]

        for i in range(numRows):
            for j in range(i+1):
                if j==0 or j==(i):
                    value=1
                    lst1.append(value)
                else:
                    lst1.append(lst2[-1][j-1]+lst2[-1][j])
            lst2.append(lst1.copy())
            del lst1[:]
        return lst2

