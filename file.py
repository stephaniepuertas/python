#this is a single line comment 
"""
this is 
multiline
comment
"""
my_new_favorite_language= 'Python' #variable declaration, inintialize string

num1 = 42 #variable declaration initialize number
num2 = 2.3 #variable declaration initialize number
boolean = True #variable declaration initialize boolean
string = 'Hello World' #variable declaration initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #composite type -list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}# composite type -dictionary 
fruit = ('blueberry', 'strawberry', 'banana')#composite type list
print(type(fruit))#common functions output class string
print(pizza_toppings[1])#output class string sausage 
pizza_toppings.append('Mushrooms') # output add pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives', 'Mushroom"] 
print(person['name']) #output print 'name':'John'
person['name'] = 'George'#updating person's name and storing it as 'George'
person['eye_color'] = 'blue' #initalizing variable person['eye_color']='blue' to dictionary
print(fruit[2])# printing banana

if num1 > 45:# conditional statement 
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5: #conditoinal statement
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5): #for loop
    print(x)
for x in range(2,5): # for loop
    print(x)
for x in range(2,10,3): #for loop
    print(x)
x = 0
while(x < 5): #while loop
    print(x)
    x += 1

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)