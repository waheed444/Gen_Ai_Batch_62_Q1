#Functions in Python
# Block of statements that perform a specific task.

def sum_calculate (a,b):     #--->def func_name( param1, param2..) :
    sum=a+b                 #--->some work
    print(sum)
    return sum              #---> return val
sum_calculate(1,4)
sum_calculate(10,40)         # func_name( arg1, arg2 ..) --->function call
sum_calculate(500,299)
# built-in functions 
print("This is a built-in function ")
#User define function 
def calculate_avg (a,b,c):
    avg=(a+b+c)/3
    print(avg)
    return sum
calculate_avg(94,67,45)

def calculate_div(a,b):
    if b!=0:
        div=a/b
        print("Division is :",div)
        return div
    else:
        print("Error! division by zero is not possible")
        return None
calculate_div(5,0)

