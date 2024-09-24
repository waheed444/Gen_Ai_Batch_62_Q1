# Recursion is nothing but used the same function inside the function 
# Recursion is the complex form of loops
# We can use recursion in function instead of loops
# Recursion helps to reduce the line of code make the program re-useble/readable. 

def show(n):    #Function defination
    if n==0:    #Condition in function
        return  #return(When condition is true)
    print(n)    #piece of code
    show(n-1)   #function call itself inside a function (Recursion)
show(5)         #call the function

# RESURSION of factorial of n number 
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
    
print(fact(5))