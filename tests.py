def calculateSum(n) :
    if (n <= 0) :
        return 0
  
    fibo =[0] * (n+1)
    fibo[1] = 1
  
    # Initialize result
    sm = fibo[0] + fibo[1]
  
    # Add remaining terms
    for i in range(2,n+1) :
        fibo[i] = fibo[i-1] + fibo[i-2]
        sm = sm + fibo[i]
         
    return sm
 
 
# Driver program to test
# above function
# print("Sum of Fibonacci numbers is : " ,
#       calculateSum(n))


# 1,1,2,3,5,8,13,21,34, 55, 
# should be 55-1= 54
#1,2,4,7,13,21,34

import math 

sum = 13

inner = (1+math.sqrt(5))/2
nth_number = math.log( (sum + 0.5 ) * math.sqrt(5)) / math.log(inner) -2

print(nth_number)
# 1,2,4,8,16,32
# 1,3,7,15,31

order = math.log(sum + 1) / math.log(2)


n = 4
print(order)