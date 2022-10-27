# Code First Girls: Python Session 1
print('Hello world')
print(50)
print(10 / 3 == 10 % 3)

# example of variables
# strings 'hellow'
# interger 100
# double 5.5

firstname = 'Yunyi'
lastname = 'Tang'
print(firstname)
print(lastname)
fullname = firstname + ' ' + lastname
print(fullname)

salary = 100
expenses = 70
savings = salary - expenses
# one way
print('Salary : ' + str(salary))
# another way
print(f'Salary : {salary}')

# exercise: We want to store customer details for kate glover's shop
# Full name
# Address
# Age

fullname = input('What is your full name? ')
address = input('What is your address? ')
age = input('What is your age? ')
agein5years = int(age) + 5

print(f'Welcome to our shop : {fullname}')
print(f'In 5 years time, you would be this years old : {agein5years}')
print('Thank for your address. Just to confirm. It is : ' + address)

# assignment
number1 = float(input('Please give me the first number '))
number2 = float(input('Please give me the second number '))
sum = number1 + number2
print(f'The summary of your numbers is {sum}')

# assignment 2
days = 31
hours = 24
total_hours = days * hours

msg = "There are {} in {} days".format(total_hours, days)
print(msg)

# Code First Girls: Python Session 2
# 1. User Input
# 2. Importing modules
# 3. For Loops
# 4. While Loops
# 5. Functions
total = 0
print("*** This statement is OUTSIDE THE LOOP")
print("Before the loop executes, our TOTAL is equal to  = ", total, '\n')
print("--------------------------------------------------------")
for number in range(3):  # remember --> 0, 1, 2
    print("This is loop execution for digit: " + str(number) + " inside the loop \n")
    print("Updating total... (+ 1) \n")
    total = total + 1  # every time the loop executes, we add 1 to the total
print("--------------------------------------------------------")
print("***This statementWe is OUTSIDE the loop now")
print("The final TOTAL value is: " + str(total))

store_capacity = 5
while store_capacity > 0:
    print('Please come in. Spaces available: ' + str(store_capacity))
    store_capacity = store_capacity - 1
print("\nPlease wait for someone to exit the store.")

# Code First Girls: Python Session 3
# 1. Comparison Operators
# 2. Logical Operators
# 3. If Statements

# Exercise 3.1: You have a budget of £10 and want to write a program to decide which burger restaurant to go to.
# 1. Input the price of a burger using input()
# 2. Check whether the price is less than or equal (<=) 10.00
# 3. Print the result in the format below
# Burger is within budget: True
# Hint: remember to convert the input from a string to a decimal with float()
price = input('What is the price? ')
within_budget = float(price) <= 10.00
print('Burger is within budget: {}'.format(within_budget))

# Exercise 3.2: Add code to your burger program to input whether the restaurant has a vegetarian option
# The output should say whether the cost is within budget AND has a vegetarian option
# Restaurant meets criteria: True
price = input('What is the price? ')
veg_option = input('Do they have vegeterian options? y/n ')
within_budget = float(price) <= 10.00
has_veg_option = veg_option == 'y'
print('Burger is within budget: {}'.format(within_budget and has_veg_option))

name = input("What is your name? ")
is_admin = name == 'admin'
password = input("What is your password? ")
password_correct = password == 'loveu'
if is_admin and password_correct:
    print('Welcome')
if not is_admin or not password_correct:
    print('No access')

# Exercise 3.3: Rewrite the output of your burger program to use if statements
# If it is a good choice it should be: This restaurant is a great choice!
# If it is not a good choice it should be: Probably not a good idea
price = input('What is the price? ')
within_budget = float(price) <= 10.00
veg_option = input('Do they have vegeterian options? y/n ')
has_veg_option = veg_option == 'y'
if within_budget and veg_option:
    print('This restaurant is a great choice!')
if not within_budget or not has_veg_option:
    print('Probably not a good idea')

password = input('password: ')
if password == 'loveu':
    print('Success!')
else:
    print('Failure!')

name = input("What is your name? ")
is_admin = name == 'admin'
password = input("What is your password? ")
password_correct = password == 'loveu'
if is_admin and password_correct:
    print('Welcome')
else:
    print('No access')

# Exercise 3.4: Now that you've nished your burger, you want to pay for your food.
# Let's write a program to calculate your meal and apply a discount if applicable.
# If your total meal costs more than £20 and you have a discount, the price will be reduced by 10%.
# The program should print "Discount applied" or "No discount" depending on whether the discount criteria was met.
meal_price = float(input('How much did the meal cost? '))
discount_choice = input('Do you have a discount? y/n ')
applicable_price = float(meal_price) > 20
discount_applicable = discount_choice == 'y'
applicable = applicable_price and discount_applicable
if applicable:
    meal_price = meal_price * 0.9
    print('Discount applied')
else:
    print('No discount')
print('Total cost: {}'.format(meal_price))

dog_size = int(input('How big is the dog? '))
if dog_size > 75:
    print('That is a big dog')
elif dog_size < 25:
    print('That is a small dog')
else:
    print('That is an average dog')

# Exercise 3.5: You're cooking a pizza and need to check that the oven is at the right temperature.
# Write a program to:
# Ask the user to input the temperature
# Prints "The oven is too hot" if the temperature is over 200
# Prints "The oven is too cold" if the temperature is under 150
# Prints "The oven is at the perfect temperature" if the temperature is 180
# Prints "The temperature is close enough" for any other temperature
temperature = int(input('What is the temperature? '))
if temperature > 200:
    print('The oven is too hot.')
elif temperature < 150:
    print('The oven is too cold.')
elif temperature == 180:
    print('The oven is at the perfect temperature.')
else:
    print('The temperature is close enough.')

# Python has a built-in library for random data
import random

random_integer = random.randint(1, 100)
print(random_integer)

# The randint() function generates a random number between two values
# This program uses randint() to simulate dice with any number of sides
import random

sides = int(input('How many sides does the die have? '))
random_integer = random.randint(1, sides)
print('You rolled a {}'.format(random_integer))

# To practice if statements choose one of the following exercises in your student guide:
# Exercise 3.6: Flip a coin
# Exercise 3.7: Rock, Scissors, Paper
# Exercise 3.8: Roulette

# Code First Girls: Python Session 4
# 1. Lists
# 2. Dictionaries

# Exercise
name = input('What is your name? ')
if name == 'Tara' or name == 'Tara ':
    print('Welcome Admin')
else:
    print('Welcome {}'.format(name))  # or print(f'Welcome {name}')

# Exercise
movies = ['pride and prejudice', 'arrival', 'twilingt', 'smile', 'interstellar']
print(f'Before appending, I have these movies: {movies}')
# methods: a piece of code that is called by name that is associated with an object
movies.append('Just Mercy')
print(f'After appending, I have these movies: {movies}')
# function: a piece of code that is called by a name
# used to find the length or size of a list
print(len(movies))
# remove from a list, .pop remove the very last item of a list
movies.pop()
print(f'After popping, we now have {movies}')

# Exercise
# We have a shop called 'Yunyi shop'. We want to add new customers to our shop
# but we need their names
# if a new customer is already an existing customer,
# we want to tell the customer they are already registered
yunyi_customers = ['Samuel']
new_customers = input('What is your name? ')
if new_customers in yunyi_customers:
    print('Oh no, you are already a customer!')
else:
    yunyi_customers.append(new_customers)
print('Now our customers are ' + str(yunyi_customers))

# Exercise
movies = ['pride and prejudice', 'arrival', 'twilingt', 'smile', 'interstellar']
first_movie = movies[0]
last_movie = movies[-1]
# three ways to find the last element:
# 1. count
# 2. length - 1
# 3. -1
print(first_movie)
print(last_movie)
movies.pop(0)
print(movies)

# Exercise
# create a list of your top 5 celebrities
# ask the user for a celebrity name.
# if the name the user gives is in your list,
# say 'You rock!' else say 'Try again'
celeb = ['a', 'b', 'c', 'd', 'e']
new_celeb = input('What is your top celebrities? ')
if new_celeb in celeb:
    print('You rock!')
else:
    print('Try again')

# Exercise
ages = [5, 12, 4, 9, 17]
under18 = []
over18 = []
for age in ages:
    if age < 18:
        under18.append(age)
    else:
        over18.append(age)
print(under18)
print(over18)

for age in ages:
    print(age)

# pre-built function
length_of_ages = len(ages)
max_ages = max(ages)
min_ages = min(ages)
sorted_ages = sorted(ages, reverse=True)

print(length_of_ages)
print(max_ages)
print(min_ages)
print(sorted_ages)

# Exercise
lunchCostsThisWeek = [5, 3, 6, 2, 8, 3, 9]
sum = 0
for lunchCost in lunchCostsThisWeek:
    sum = sum + lunchCost
print(sum)  # or print(sum(lunchCostsThisWeek))

# Exercise
person = {}
person['name'] = input('What is your name? ')
person['address'] = input('What is your address? ')
print(person)

# Assignment
# You are the owner of Yunyi shop. You have a customer in front of you
# and you want to store that customer's details (e.g name, age, phone) in an
# object/dictionary. If the age of the customer is > 60, assign 'Senior Citizen' to
# the 'citizen' attribute in the object/dictionary.
# If not, assign 'Junior Citizen'
# Create a program that does this
yunyi_customers = {}
yunyi_customers['name'] = input('What is your name? ')
yunyi_customers['phone'] = input('What is your phone number? ')
yunyi_customers['age'] = int(input('What is your age? '))
if yunyi_customers['age'] > 60:
    yunyi_customers['citizen'] = 'Senior Citizen'
else:
    yunyi_customers['citizen'] = 'Junior Citizen'
print(yunyi_customers)

# nesting objects
place = {
    'name': 'The Anchor',
    'post_code': 'E14 6HY',
    'street_number': '54',
    'location': {
        'longitude': 127,
        'latitude': 63,
    }
}

# IndexError: list index out of range
cheeses = [
    'brie',
    'cheddar',
    'wensleydale',
    'edam',
]
print(cheeses[4])

# SyntaxError: '[' was never closed
trees = [
    {'leaf_colour': 'green', 'height': 2120},
    {'leaf_colour': 'green', 'height': 2300}]
new_tree = {
    'leaf_colour': 'green',
    'height': 1020
}
trees.append(new_tree)
print(trees)

# Random
import random

colours = ['red', 'green', 'blue']
chosen_colour = random.choice(colours)
print(chosen_colour)

# Code First Girls: Python Session 5
# 1. Files
# 2. Pip package manager
# 3. APIs

# Writing to a file
new_item = input('Enter a to-do item: ')
with open('todo.txt', 'r') as todo_file:
    todo = todo_file.read()
    todo = todo + new_item + '\n'
with open('todo.txt', 'w+') as todo_file:
    todo_file.write(todo)

# Exercise 5.2: This program is supposed to read data about trees from a
# file to find the shortest tree.
import csv

with open('trees.csv') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    heights = []
    for row in spreadsheet:
        tree_height = row['height']
        heights.append(tree_height)

shortest_height = min(heights)
print(shortest_height)
