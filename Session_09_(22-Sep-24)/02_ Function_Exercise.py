# WAF to print the length of a list. ( list is the parameter)
# WAF to print the elements of a list in a single line. ( list is the parameter)
list=['waheed','ahmad','ali','abdulla','hassan','car','bycycle','motercar']
def len_list(list):
    for i in list:
        print(i)
    print("These are above",len(list),"list items")
    print("All list items in one line are")
    print(" ".join(list))   #Print the list items in single line 
    return list
len_list(list)
#WAF to find the factorial of n. (n is the parameter)
n=5
fact=1
for i in range(1,n+1):
    fact*=i
print(f" factorial of {n} is : {fact}")   #using f-string here

# WAF to convert USD to PKR

def convertor(usd_value):
    pkr_value=usd_value*278
    print(usd_value,"USD = ",pkr_value,"PKR ")
convertor(100)

def even_odd(n):
    if n%2==0:
        print(f"{n} is Even")
        return n
    else:
        print(f"{n} is odd")
even_odd(999933)



