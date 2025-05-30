str1=['flower','flow','float']
var=''
i=0

var2=len(str1[0])

#Length of the shortest Element from the Array
while(i<len(str1)):
    if len(str1[i])<var2:
        var2=len(str1[i])
        i+=1
    else:
        i+=1
#Calculating Longest Common Prefix
i=1
j=0
while(j<var2):
    for i in range(len(str1)):
        if str1[i][j]!=str1[0][j]:
            j=var2
            break
    else:
       var+=str1[0][j]
    j+=1
print('Longest Common Prefix:',var)
