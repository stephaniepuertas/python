
# 1) Update Values in Dictionaries and Lists
#     1-Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
#     2-Change the last_name of the first student from 'Jordan' to 'Bryant'
#     3-In the sports_directory, change 'Messi' to 'Andres'
#     4-Change the value 20 in z to 30

x = [ [5,2,3], [10,8,9] ] 

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# answer:
# Question #1
x[1][0]= 15
print (x)

# Question #2
students [0]["last_name"]="Bryant"
print (students)

# Question #3
sports_directory['soccer'][0]="Andres"
print (sports_directory)

# Question #4
z[0]['y']= 30
print (z)


# # 2- Iterate Through a List of Dictionaries
# create a function iterateDictionary(some_list) that, given a list of dictionaries, 
# the function loops through each dictionary in the list and prints each key and 
# #     # the associated value. For example, given the following list:
students =[
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


def iterateDictionary(some_list):
    for item in some_list:
        for key in item:
            print (key,item[key])
iterateDictionary(students)

# another way to write the same thing
# def iterateStudents():
#     for student in students:
#         for name in student:
#             print (name,student[name])
# iterateStudents()

# name of dictionary [name key ]

# # should output: (it's okay if each key-value pair ends up on 2 separate lines;


# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


# # 3- Get Values From a List of Dictionaries

# Create a function iterateDictionary2(key_name, some_list) 
# that, given a list of dictionaries and a key name, the function prints the value 
# stored in that key for each dictionary. 
# For example, iterateDictionary2('first_name', students) should output:


# def iterateDictionary(some_list):
#     for item in some_list:
#         for key in item:
#             print (key,item[key])
# iterateDictionary(students)

# # DEFINE FUNCTION
def iterateDictionary2(key_name, some_list):
    for student in some_list:
        print(key_name,student[key_name])


# # CALL FUNCTOIN
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)


# # # 4 -Iterate Through a Dictionary with List Values
# #     # Create a function printInfo(some_dict) that given a dictionary whose values 
# #     # are all lists, prints the name of each key along with the size of its list, 
# #     # and then prints the associated values within each key's list. For example:

dojo = {
    'locations': [
        'San Jose',
        'Seattle',
        'Dallas',
        'Chicago',
        'Tulsa',
        'DC',
        'Burbank'],
    'instructors':[
        'Michael',
        'Amy',
        'Eduardo',
        'Josh',
        'Graham',
        'Patrick',
        'Minh',
        'Devon']
}

def print_info(dict_input):
    for key in dict_input.keys():
        print(f'{len(dict_input[key])}{key}')
        for element in dict_input[key]:
            print(element)
print_info(dojo)


# # printInfo(dojo)
# # # output:
# #  7 LOCATIONS
# # San Jose
# # Seattle
# # Dallas
# # Chicago
# # Tulsa
# # DC
# # Burbank


# # # 8 INSTRUCTORS
# # Michael
# # Amy
# # Eduardo
# # Josh
# # Graham
# # Patrick
# # Minh
# # Devon
