class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        else:
            mid=numRows-2
            i=0
            j=2
            var=numRows+mid
            result=''
            while True:
                    try:
                        result+=s[i]
                        i+=var
                    except IndexError:
                        break

            for i in range(1,numRows-1):
                while True:
                    try:
                        result+=s[i]
                        i+=var-j
                        result+=s[i]
                        i+=var-(var-j)
                    except IndexError:
                        break
                j+=2
            i=numRows-1
            while True:
                    try:
                        result+=s[i]
                        i+=var
                    except IndexError:
                        break
            return result 

    
        
