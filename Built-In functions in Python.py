#built in functions

from math import *
#abs() function

number=-120
print(abs(number))

#len() function

name_1='sam'
name_2="JOSH"
print(len(name_1))

#upper()function

print(name_1.upper())

#lower() function
print(name_2.lower())

#replace function

print(name_1.replace(name_1,name_2))

#String Function

#print(str(number)/2)
# #we should get an error because number is now a string not an integer


#int function

numberString='1200'

print(int(numberString)/3)

#float function

print(float(numberString)/4.5)

#power function

base=5
power=2

print(pow(base,power))

#max function returns the greatest value in a list

Num1=24.8
Num2=25.2
Num3=25.1
print("the greatest value is ",max(Num1,Num2,Num3))
#Min function returns the smallest value in a list

print("the smallest value in the list is ",min(Num1,Num2,Num3))

#round function

Num4= 4.67
print(round(Num4))

Num5=5.6787556
print(round(Num5,3))#here we defined the limit of the numbers we can take after the decimal point

#sqrt function

Num6=4

print(sqrt(Num6))


#floor function

Num7=4.7

print(floor(Num7))

#Substring function

City="Baghdad"
print(City[0:3])

#help function

#print(help())

#range function

for numbers in range(1,100):
    print(numbers)

# the 3 means that the function skips every 3 indexes
for Skips in range(1,100,2):
    print(Skips)



    #Slice Function

    List=[100,200,300,400,500,600,700,800]
    SlicedList=slice(1,5)

    print(List[SlicedList])

    #Slice and skip indexes
List=[100,200,300,400,500,600,700,800]
SlicedList=slice(1,5,2)

print(List[SlicedList])






