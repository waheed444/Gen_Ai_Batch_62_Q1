#Assignment # 03 (Variables/Strings)
#WAHEED AHMAD  (Roll no: PIAIC-245268)
#1 Simple Message
var="python"
print(var)

#2 Simple Messages
msg="class-Python"
print(f"This is a new message, we learned something about python in our {msg}")

#3 Personal essage
person_name="WAHEED AHMAD"
print(f"Hello {person_name}, would you like to learn some python today?")

#4 Name Cases
name="PROF ZIA KHAN"
print (name.upper(), name.title(), name.lower())

#5 Famous Qoute
print("IMRAN KHAN says, \"Compromise for you dream but never compromise on your dream\"")

#6 Famous Qoute 2
famous_person="IMRAN KHAN"
print(f"{famous_person} once said, \"The more you study, the more you know; how less you know\"")

#7 Stripping Names
person = "  Prof Zian Khan   "
print(person)             #normal print
print(person.rstrip())    #remove witespaces from right side
print(person.lstrip())    #remove witespaces from left side
print(person.strip())     #remove witespaces from  both side

#8 Variable Sum
X =10
Y =20
Z =30
print(X+Y+Z)    # Resuslt = 10+20+30=60

#9 Variable Swap
a="20"
b="50"
print(f"Before Swapping: {a}  {b}")
a=b
b=a
print(f"After Swapping:  {a}  {b}")

#10 Favorite color
color ="Green"
print(f"My favorite color is {color}")
new_color=color
print(f"My favorite color is {new_color}")

#11 Changing Pet Name
pet_name="buddy"
print(f"My pet name is {pet_name}")
pet_name="max"
print(f"My pet name is {pet_name}")

#12 Observing Name Error
sunshine="HELLO SUNSHINE"
# print(Sunshine)  # Error! Sunshine is not defined

#13 Reassigning Score
score=100
print(score)
score=200
print(score)

#14 City Name
city ="Lahore"
print(city)

#15 Title Case Text
text ="python programming"
print(text.title())

#16 Lowercase Conversion
script ="pYthOn prOGRamming"
print(script.lower())

#17 Uppercase Conversion
script2 ='pHYTon PRogrMinG'
print(script.upper())

#18 Current Temperature
temperature =25
print(f"\"The current temperature is :{temperature} degrees.\"")

#19 Printing a Poem
Poem = """Nature's first green is gold,
Her hardest hue to hold.
Her early leaf's a flower;
But only so an hour."""
print(Poem)

