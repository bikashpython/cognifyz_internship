# Fibonacci Sequence
n = int(input("Enter num,ber of terms: "))

a , b = 0 , 1
count = 0
while count < n:
    print(a , end= " ")
    a, b = b, a + b
    count +=1