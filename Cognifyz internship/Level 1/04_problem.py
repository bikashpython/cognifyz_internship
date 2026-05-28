# Calculator Program
a = float(input("Enter your First Number: "))
b = float(input("Enter your second Number: "))

print(f"{a} + {b} =  {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} X {b}  = {a * b}")


if b != 0:
    print(f"{a} / {b} = {a / b}")
else:
    print("Division by zero is not allowed ")