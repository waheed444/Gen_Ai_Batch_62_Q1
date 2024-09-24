#write a Resursian function to find the sum of first n natural numbers: 

def sum_cal(n):
    if n==0:
        return 0
    print(n)
    sum_cal(n-1)
sum_cal(5)


def sum_cal(n):
    if n==0:
        return 0
    return sum_cal(n-1)+n  # return + function call itself + n 
    
print(sum_cal(5))


# write a recursion function to print the list item by their index 
def print_list(list,index=0):
    if index==len(list):
        return
    print(list[index])
    print_list(list,index+1)

name=['waheed','ahmad','ali','abdullah','hassan','car','bycycle','motercar']
print_list(name)