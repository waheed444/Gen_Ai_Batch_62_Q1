# Excersie # 3-1 Names:
names = ['waheed','ali','ahmad','amir']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print("---------------------------------------")
# Excersie # 3-2 Greetings:
msg = 'Hello! How are you?'
print(f'{names[0]} {msg} ')
print(f'{names[1]} {msg} ')
print(f'{names[2]} {msg} ')
print(f'{names[3]} {msg} ')
print("---------------------------------------")
# Excersie # 3-3 Your Own List:
Fav_bikes = ['I want to buy RBR','I want to buy Suzuki','I want to buy Honda']
for elements in Fav_bikes:
    print (elements)
print("---------------------------------------")    
# Excersie # 3-4 Gust List:
guests = ['waheed','ali','ahmad','amir']
message = "I want to invite you in dinner today"
for names in guests:
    print(f'Dear \"{names}\" , {message}')
print("---------------------------------------")    
# Excersie # 3-5 Changing Guest List
print(f'Oh, Dear {guests[1]} cant make it to dinner')
guests[1] = 'Hassan Ali'
for names in guests:
    print(f'Dear \"{names}\" , {message}')
print("---------------------------------------")
# Excersie # 3-6 More Guest
guests.insert(0,'Ahad')
guests.insert(2,'Zain')
guests.append('hassan')
for names in guests:
    print(f'Dear \"{names}\" , {message}')
print("---------------------------------------")  
# Excersie # 3-7 Shrinking Guest List:  
my_list = ['waheed', 'ali', 'ahmad', 'amir']

del my_list[2:4]  # Removes elements at index 2 and 3
print(my_list)  # Output: ['waheed', 'ali']
print("---------------------------------------")  
# Excersie # 3-8 Seeing the World:
places_to_visit = ["pakistan", "UK", "UAE", "USA", "China"]
print("Original list:",places_to_visit)                       # Print the list   
print("\nList in alphabetical order (using sorted()):")       # Use sorted()
print(sorted(places_to_visit))
print("\nList after sorted(), still in original order:")     # Still in its original order
print(places_to_visit)
# Use sorted() to print the list in reverse-alphabetical order without modifying the original list
print("\nList in reverse-alphabetical order (using sorted()):")
print(sorted(places_to_visit, reverse=True))
print("\nList after reverse-sorted(), still in original order:") # Still in its original order
print(places_to_visit)
places_to_visit.reverse()                   #  Use reverse()
print("\nList after reverse():")
print(places_to_visit)
#  Use reverse() to change the order of the list again to bring it back to the original order
places_to_visit.reverse()        
print("\nList after reverse() again to restore original order:")
print(places_to_visit)
#  Use sort() to change the list so it’s stored in alphabetical order
places_to_visit.sort()
print("\nList after sort() in alphabetical order:")
print(places_to_visit)
#  Use sort() to change the list so it’s stored in reverse-alphabetical order
places_to_visit.sort(reverse=True)
print("\nList after sort() in reverse-alphabetical order:")
print(places_to_visit)
print("---------------------------------------") 
# Excersie # 3-9 Every Function:
#  Create a list of programming languages
languages = ["Python", "C++", "Java", "JavaScript", "Ruby"]
#  Print the original list
print("Original list:",languages)
#  Access an individual element from the list
print("\nAccessing the first element in the list:")
print(languages[0])
#  Modify an element in the list
languages[2] = "Kotline"
print("\nList after modifying the third element (Java -> C#):",languages)
#  Add an element to the end of the list using append()
languages.append("C-Sharp")
print("\nList after appending a new language (C-Sharp):",languages)
#  Insert an element at a specific position in the list
languages.insert(1, "Swift")
print("\nList after inserting a language (Swift) at position 1:",languages)
#  Remove an element from the list using del statement
del languages[3]
print("\nList after deleting the fourth element (JavaScript):",languages)
#  Remove an element by value using remove()
languages.remove("Ruby")
print("\nList after removing an element by value (Ruby):",languages)
#  Pop an element from the list and use it
popped_language = languages.pop()
print("\nList after popping the last element:")
print(languages)
print(f"Popped element: {popped_language}")
#  Pop an element from a specific position in the list
popped_language = languages.pop(2)
print("\nList after popping the third element:")
print(languages)
print(f"Popped element: {popped_language}")
#  Sort the list alphabetically with sort()
languages.sort()
print("\nList after sorting alphabetically with sort():")
print(languages)
#  Sort the list in reverse alphabetical order with sort(reverse=True)
languages.sort(reverse=True)
print("\nList after sorting in reverse alphabetical order with sort(reverse=True):")
print(languages)
#  Reverse the order of the list with reverse()
languages.reverse()
print("\nList after reversing the order with reverse():")
print(languages)
print("---------------------------------------") 
# Excersie # 3-10 Intentional Error:
lang = ["Python", "C++", "Java", "JavaScript", "Ruby"]
# print(lang[6])   #Error occur because index{6} does not exist