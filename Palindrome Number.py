class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num=str(x)
        flag=True
        if len(num)==1:
            flag=True
            return flag
        else:
            j=len(num)-1
            for i in range(len(num)/2): 
                if num[i] == num[j]:
                    j-=1    
                else:
                    flag=False
                
            if flag==False:
                return False
            else:
                return True  
               
    
        

        
