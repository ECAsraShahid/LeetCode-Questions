def function(num1,num2):
    sum1=0
    sum2=0
    for i in range(1,num1+1):
        if i%num2 != 0:
            sum1+=i
        if i%num2 == 0:
            sum2+=i
    print('Divisible and Non-divisible Sums Difference:',sum1-sum2)

function(5,6)
            
            
