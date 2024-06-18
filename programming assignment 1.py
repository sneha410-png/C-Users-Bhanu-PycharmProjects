# PROGRAMMING ASSIGNMENT 1

#1 Write a program that takes two numbers as input and prints their sum.
num1=input("enter  the first  number ")
print(num1)
num2=input("enter the second number")
print(num2)
add=int (num1)+int (num2)
print( "the sum of numbers is",add)

#2 Write a python program that checks whether a given number is even or odd.
number=int(input( "enter the number"))
if(number % 2)==0:
    print("the number is even ")
else:
    print("the number is odd")
#3 Write a python program that calculates the factorial of a given number.
num=int(input("enter a number:"))
fact=1
# num=0 or 1
if (num==0) or (num==1):
    print(" the factorial is 1")
elif num<0:
    print("cannot factorial for negative number:")
else:
    while(num>0):
        fact=fact*num
        num=num-1
        print("the factorial of the number :",fact)

#4 Write a program that asks the user for their name and then prints a greeting message.
name=str(input("enter your name "))
print("hello ",name)
#5 Write a program that takes a string input from the user and writes it to a text file
samplefile=open('F:/Summer Intern 2nd year Python and ML/demo.txt','w')
n=str(input("enter your name "))
print(n, file=samplefile)


#6 Write a program that reads the content of a text file and prints it to the console.samplefile=open('F:/Summer Intern 2nd year Python and ML/demo.txt','r')




#7 Write a python program that takes a string as input and returns its length.
s=str(input("enter the name of the user "))
print(s)
print(len(s))
#8 Write a python program that concatenates two strings and returns the result.
str=("Sneha Verma")
str1=("studying in IGDTUW")
str2=str+str1
print(str2)
#9 Write a python program that checks if a substring is present in a given string




#10. Write a python program that converts a given string to uppercase.
program=("programmming is one of the hardest i have ever found in my system")
p=program.upper()
print(p)
#11. Write a python program that generates the first n numbers in the Fibonacci sequence.


#12. Write a python program that calculates the sum of the digits of a given number.
number=int(input("enter the number "))
print("the entered number is ",number)
sum=0
while(number!=0):
    sum=sum+(number%10)
    number=number//10
    print(sum)
#13. Write a program that asks the user for their birth year and calculates their age.
from datetime import datetime
def calculateage(birthdate):
    today=datetime.today()
    age=today.year-birthdate.year-((today.month,today.day)<(birthdate.month,birthdate.day))
    return age
dob_input=input("enter the age (YYYY-MM-DD):")
birthdate = datetime.strptime(dob_input, "%Y-%m-%d")
age=calculateage(birthdate)
print("your age is {age} years",age)
#14. Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.
#15. Write a program that reads data from a CSV file and prints it to the console.
#16. Write a program in python that counts the frequency of each character in a string.
#17. Write a program in python that converts a given string to title case (first letter of each word capitalized).
#18. Write a python program that checks if two strings are anagrams of each other.
#19. Write a python program that removes all punctuation from a given string.
#20. Write a python program that takes a list of numbers and returns their sum.
#21. Write a python program that counts the occurrences of a specific element in a list.
#22. Write a python program that returns the minimum and maximum values in a list of numbers.
#23. Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.
#24. Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.

#25. Write a program that copies the contents of one text file to another.

#26. Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.
#27. Write a program in python that converts a string into a list of its characters.'''
list1=[1,2,3,4,"hello",True,False]
for i in list1:
    print("the value in list is: " ,i)