# loop

# DRY 

# while condition:
#     statement

# i = 0 
# while i < 5:
#     print('Hello World')
#     i = i + 1

# infinite loop
    # runs forever
   
# names = ['ram', 'shyam', 'hari', 'rita', 'ramesh']
# i = 0
# while i < len(names):
#     print(names[i])
#     i = i + 1

# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i += 1



# i = 0
# while i < 6:
#     i += 1
#     if i % 2 == 0:
#         continue
#         print(i)
#     print(i)


# string, list, set, tuple, dictionary

# for variable_name in iterables:
#     statement

# for item in 'ramesh':
#     print(item)
#     print('**')

# for val in ['ram', 'shyam', 'hari']:
#     print(val)

# for val in ('ram', 'shyam', 'hari'):
#     print(val)


grades = {'ram': 25, 'shyam': 30, 'hari': 60}
# for val in grades:
#     print(val)

# for val in grades.keys():
#     print(val)

# for val in grades.values():
#     print(val)

# print(grades.keys())
# print(grades.values())
# print(grades.items())

# [('ram', 25), ('shyam', 30), ('hari', 60)]

# for val in grades.items():
#     print(val)

# for k,v in grades.items():
#     print(k, v)

# -------------
# group of statments that together performs specific task.
# function creates reusable logic


# def function_name():
#     pass


# functional definition/declaration
# def add():
#     print(1+1)

# add()
# add()
# add()

# def add(i,j):
#     print(i+j)

# add(5,3)
# add(2,3)
# add(2,4)

# types of arguments    
    # positional arguments
        # order of the arguments matter

    # keyword arguments
        # oder of the arguments does not matter

    # default
        # a default value if provived

# def info(fn, ln, age):
#     print(f'Hello {fn} {ln}. Your age is {age}')

# info('ram', 'hari', 25)
# info(25, 'hari', 'ram')


# def info(fn, ln, age):
#     print(f'Hello {fn} {ln}. Your age is {age}')

# info(age=25, ln='hari', fn='ram')

def info(fn, ln, age, balance=0):
    print(f'Hello {fn} {ln}. Your age is {age}')
    print(f'Your balance is {balance}')

info(age=25, ln='hari', fn='ram')
info(age=25, ln='hari', fn='ram', balance=100)






