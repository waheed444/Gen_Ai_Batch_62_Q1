# Sometimes a programmer wants to execute a group of statements a certain number of times. This can be done using loops.
# Based on this loops are further classified into following main types;
# for loop
# while loop
name = "Waheed"
for i in name:     #print each alphabet of string in name by for loop
    print(i)       #print i

#print the colors in the form of list
#List always be in square brackets '[]'
color = ["red","green","blue","purple","white","black"] 
for color in color:
    print(color)
    #print each alphabet of string in color  
    for i in color:
        print(i)
# What if we do not want to iterate over a sequence?
# What if we want to use for loop for a specific number of times?
# Here, we can use the range() function.
#range started from 0 index to n-1 index (for range 5 -->  '0 to 4 ')
for k in range(10):
    print(k)
#range can contains arrguments (print 1 to 8)    
for m in range(1,9):
    print(m)
# "+1" means it start from 1 and includes the last index 'n' not 'n-1'    
for m in range(10):
    print(m+1)
#range function has three parameters
#Start(from 1) , Stop(at 12),Step(jump of 3)    
for n in range(1,12,3):
    print(n)     
    