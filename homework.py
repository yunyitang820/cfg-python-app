# Code First Girls: Python Session 1 
# Question 1
# I am building some very high quality chairs and need exactly four nails for each chair.
# I've written a program to calculate how many nails I need to buy to build these chairs.
chairs = 15
nails = 4
total_nails = chairs * nails
message = 'I need to buy {} nails'.format(total_nails)
print('You need to buy {} nails'.format(message))
# When I run the program it tells me that I need to buy 15151515 nails.
# This seems like a lot of nails.
# Is my program calculating the total number of nails correctly? What is the problem? How do I fix it?

# Question 2
# I'm trying to run this program, but I get an error.
# What is the error telling me is wrong? How do I fix the program?
my_name = 'Penelope'
my_age = 29
message = 'My name is {} and I am {} years old'.format(my_name, my_age)
print(message)

# Question 3
# I have a lot of boxes of eggs in my fridge and I want to calculate how many omelettes I can make.
# Write a program to calculate this.
# Assume that a box of eggs contains six eggs and I need four eggs for each omelette,
# but I should be able to easily change these values if I want.
# The output should say something like "You can make 9 omelettes with 6 boxes of eggs".
eggs_per_box = int(input('How many eggs per box did you buy? '))
number_eggs_boxes = int(input('How many boxes of eggs do you have? '))
number_eggs = number_eggs_boxes * eggs_per_box
each_omelette = 4
number_omelette = int(number_eggs/each_omelette)
number_omelette_msg = 'You can make {} omelettes with {} boxes of eggs'.format(number_omelette, number_eggs_boxes)
print(number_omelette_msg)

# Code First Girls: Python Session 2
# Question 1
# Explain what this program does
for number in range(100):
    output = 'o' * number
print(output)

# Question 2
# Your boss really likes calculating VAT on their purchases. It is their favourite hobby.
# They've written this code to calculate VAT and need your help to fix it.
def calculate_vat(amount):
    return amount * 1.2
total = calculate_vat(100)
print(total)
# When your boss runs the program they get the following output: None
# Your boss expects the program to output the value 120. What is wrong? How do you fix it?

# Code First Girls: Python Session 3
# Question 1
# Create a program that tells you whether or not you need an umbrella when you leave the house.
# The program should:
# 1. Ask you if it is raining using input()
# 2. If the input is 'y', it should output 'Take an umbrella'
# 3. If the input is 'n', it should output 'You don't need an umbrella'
raining = input('Is it raining? y/n ')
if raining == 'y':
    print('Take an umbrella.')
else:
    print('You don\'t need an umbrella')


# Question 2
# I'm on holiday and want to hire a boat. The boat hire costs £20 + a refundable £5 deposit. I've
# written a program to check that I can afford the cost, but something doesn't seem right.
# Have a look at my program and work out what I've done wrong
my_money = int(input('How much money do you have? '))
boat_cost = 20 + 5
if my_money < boat_cost:
    print('You can afford the boat hire')
else:
    print('You cannot afford the board hire')

# Question 3
# Your friend works for an antique bookshop that sells books between 1800 and 1950 and wants to
# quickly categorise books by the century and decade that they were written.
# Write a program that takes a year (e.g. 1872) and outputs the century and decade
# (e.g. "Nineteenth Century, Seventies")
def decade_to_text(decade):
    if decade >= 90:
        return 'Nineties'
    elif decade >= 80:
        return 'Eighties'
    elif decade >= 70:
        return 'Seventies'
    elif decade >= 60:
        return 'Sixties'
    elif decade >= 50:
        return 'Fifties'
    elif decade >= 40:
        return 'Forties'
    elif decade >= 30:
        return 'Thirties'
    elif decade >= 20:
        return 'Twenties'
    elif decade >= 10:
        return 'Tens'
    else:
        return 'Hundreds'
written_year = int(input('Which year this book was wrote? From 1800 to 1950 '))
decade = written_year % 100
if written_year < 1800 or written_year > 1950:  # further refine on generosity
    print('Sorry, this book is not sold at this antique bookshop.')
elif written_year // 100 == 19:
    century = 'Twentieth Century'
    print(century + ', ' + decade_to_text(decade))
elif written_year // 100 == 18:
    century = 'Nineteenth Century'
    print(century + ', ' + decade_to_text(decade))

# written_year = int(input('Which year this book was wrote? From 1800 to 1950 '))
# if written_year >= 1900 and written_year <= 1950:
#     century = 'Twentieth Century'
#     decade = written_year - 1900
# if written_year >= 1800 and written_year <1900:
#     century = 'Nineteenth Century'
#     decade = written_year - 1800
# def decade_to_text(decade):
#     if decade >= 90:
#         return 'Nineties'
#     elif decade >= 80:
#         return 'Eighties'
#     elif decade >= 70:
#         return 'Seventies'
#     elif decade >= 60:
#         return 'Sixties'
#     elif decade >= 50:
#         return 'Fifties'
#     elif decade >= 40:
#         return 'Forties'
#     elif decade >= 30:
#         return 'Thirties'
#     elif decade >= 20:
#         return 'Twenties'
#     elif decade >= 10:
#         return 'Tens'
#     else:
#         return 'Hundreds'
# if written_year >= 1800 and written_year <= 1950:
#     print(century + ', ' + decade_to_text(decade))
# else:
#     print('Sorry, this book is not sold at this antique bookshop.')

# if written_year == 1950:
#     print('Twentieth Century, Fifties')
# elif written_year < 1950 and written_year >= 1940:
#     print('Twentieth Century, Forties')
# elif written_year < 1940 and written_year >= 1930:
#     print('Twentieth Century, Thirties')
# elif written_year < 1930 and written_year >= 1920:
#     print('Twentieth Century, Twenties')
# elif written_year < 1920 and written_year >= 1910:
#     print('Twentieth Century, Tenth')
# elif written_year < 1910 and written_year >= 1900:
#     print('Twentieth Century, Hundreds')
# elif written_year < 1950 and written_year >= 1940:
#     print('Twentieth Century, Forties')
# elif written_year < 1940 and written_year >= 1930:
#     print('Twentieth Century, Thirties')
# elif written_year < 1930 and written_year >= 1920:
#     print('Twentieth Century, Twenties')
# elif written_year < 1920 and written_year >= 1910:
#     print('Twentieth Century, Tens')
# elif written_year < 1910 and written_year >= 1900:
#     print('Twentieth Century, Hundreds')
# elif written_year < 1900 and written_year >= 1890:
#     print('Nineteenth Century, Nineties')
# elif written_year < 1890 and written_year >= 1880:
#     print('Nineteenth Century, Eighties')
# elif written_year < 1880 and written_year >= 1870:
#     print('Nineteenth Century, Seventies')
# elif written_year < 1870 and written_year >= 1860:
#     print('Nineteenth Century, Sixties')
# elif written_year < 1860 and written_year >= 1850:
#     print('Nineteenth Century, Fifties')
# elif written_year < 1850 and written_year >= 1840:
#     print('Nineteenth Century, Forties')
# elif written_year < 1840 and written_year >= 1830:
#     print('Nineteenth Century, Thirties')
# elif written_year < 1830 and written_year >= 1820:
#     print('Nineteenth Century, Twenties')
# elif written_year < 1820 and written_year >= 1810:
#     print('Nineteenth Century, Tens')
# elif written_year < 1810 and written_year >= 1800:
#     print('Nineteenth Century, Hundreds')

# Code First Girls: Python Session 3
# Question 1
# I have a list of things I need to buy from my supermarket of choice.
shopping_list = [
    "oranges",
    "cat food",
    "sponge cake",
    "long-grain rice",
    "cheese board",
    ]
print(shopping_list[0])
# I want to know what the first thing I need to buy is. However, when I run the program it shows me a
# different answer to what I was expecting?
# What is the mistake? How do I fix it?

# Question 2
# I'm setting up my own market stall to sell chocolates. I need a basic till to check the prices of
# different chocolates that I sell.
# I've started the program and included the chocolates and their prices. Finish the program by asking
# the user to input an item and then output its price.
chocolates = {
    'white': 1.50,
    'milk': 1.20,
    'dark': 1.80,
    'vegan': 2.00,
    }
request = input('What chocolates do you want? white/milk/dark/vegan ')
print('The price of this chocolates is ' + str(chocolates[request]) + '.')

# Question 3
# Write a program that simulates a lottery. The program should have a list of seven numbers that
# represent a lottery ticket. It should then generate seven random numbers. After comparing the two
# sets of numbers, the program should output a prize based on the number of matches:
# ● £20 for three matching numbers
# ● £40 for four matching numbers
# ● £100 for five matching numbers
# ● £10000 for six matching numbers
# ● £1000000 for seven matching numbers

import random
lottery_range = range(50)

def draw():
    win_ticket = [random.randrange(1, 50), random.randrange(1, 50), random.randrange(1, 50), random.randrange(1, 50),
                  random.randrange(1, 50), random.randrange(1, 50), random.randrange(1, 50)]
    return win_ticket
print("Lucky Numbers:", draw())

your_ticket = [1, 3, 5, 7, 9, 11, 13]
win_ticket = draw()

def compare():
    matches = []
    for num in your_ticket:
        if num in win_ticket:
            matches.append(num)
    if len(matches) == 3:
        print('You WIN £20 for three matching numbers')
    elif len(matches) == 4:
        print('You WIN £40 for four matching numbers')
    elif len(matches) == 5:
        print('You WIN £100 for five matching numbers')
    elif len(matches) == 6:
        print('You WIN £10,000 for six matching numbers')
    elif len(matches) == 7:
        print('You WIN £1,000,000 for seven matching numbers!')
    else:
        print('You win nothing. Try again!')

compare()
