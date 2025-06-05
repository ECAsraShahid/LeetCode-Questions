class Solution:
    def reverse(self, x: int) -> int:
        z=''
        if x<0:
            x*=(-1)
            z+='-'
            
        y=list(map(int,str(x)))
        x=y[::-1]
        if len(x)==1 and x[0]==0:
            z+=str(x[0])
        else:
            try:
                i=0
                while x[i]==0:
                    x.remove(x[i])
                    
            except IndexError:
                i-=1
        for i in x:
            z+=str(i)
        if z=='':
            z+='0'
        x=int(z)
        if x< -2**31 or x> (2**31) - 1:
            return 0
        else:
             return x

