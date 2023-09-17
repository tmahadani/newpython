a=22
b=33
total=a+b
print(total)

number1 = int(input("please enter a number"))
number2 = float(input("please enter a another number"))
total = (number1 + number2)
print(total)

a = 7%5
print(a)

a = int(input("please enter a first number"))
b = int(input("please enter a second number"))
c = int(input("please enter a third number"))
total = (a+b+c)
print(total)
average = total/3
print(average)

a = int(input("please enter a first number"))
b = int(input("please enter a second number"))
c = int(input("please enter a third number"))
total = (a+b+c)
average = total/3
print("Total:", total, "Average:", average)

for counter in range (10):
    print(counter)

for i in range (10):
    print(i)

for i in range(3, 21):
    print(i)

for i in range(2, 21, 5):
    print(i)


## multiplication table
number = int(input('What time table do you want to display?'))
##use a for loop to print the time table
for i in range(1, 13):
    result = i*number
    print(f"{i} x {number} = {result}")

##
msg = input("please enter a massage ")
no_of_times = int(input("How many times would you like to print massage?"))
for i in range(1, no_of_times + 1):
    print(f"{i}. {msg}")


##simple password checker
entry = ""
password = "let mein"
while entry != password:
    entry = input("please enter your password")

##infinite loop
guess = ''
while guess !="Tanu":
    guess = input('Guess my name: ')
print('Bravo! you guessed correctly')

## while loop with break
while True:
    guess = input('Guess my name')
    if guess =='Tanu':
        print('correct')
        break
    print('wrong')

## while loop with break and continue
while True:
    guess = input('Guess my name')
    if guess !='Tanu':
        print('Wrong')
        continue
    print('Correct!')
    break

##ask the user for two numbers
first_number = int(input("please enter the first number:"))
second_number = int(input("please enter the second number:"))
if first_number > second_number:
    print("the first number is greater than the second number")
elif first_number == second_number:
    print('Both number are equal')
else:
    print('The second number is geater than first number')

    
    
##leap year calculation
birth_year = int(input('please enter your birth year'))
if(birth_year%4 == 0):
    print('you wre born in leap year')
else:
    print('you wre not born in aleap year')