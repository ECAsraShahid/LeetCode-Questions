I=1
V=5
X=10
L=50
C=100
D=500
M=1000
num=input('Enter the roman number:')
res=0
i=0
while True:
    try:
        if i==len(num)-1:
            res+=eval(num[i])
            i+=1
        elif eval(num[i])<eval(num[i+1]) :
            print('i',i)
            
            res+=eval(num[i+1])-eval(num[i])
            print('res',res)
            i+=2
        else:
             res+=eval(num[i])
             i+=1
        
        
    except IndexError:
        break
print(res)
