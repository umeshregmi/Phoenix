# runtime errors/ exception
    # unwanted termination of program happens.
    # program crashes

# while True:
#     a = int(input('Enter first number '))
#     b = int(input('Enter second number '))
#     print(f'{a} divided by {b} is {a/b}')

try:
    # risky code 
    # code that can throw errors
    pass
except:
    # alternative code
    # code to run when there is an error
    pass
finally:
    # optional
    # runs always
    pass


# while True:
#     try:
#         a = int(input('Enter first number '))
#         b = int(input('Enter second number '))
#         print(f'{a} divided by {b} is {a/b}')
#     except ZeroDivisionError:
#         print('second number cannot be 0')
#     except ValueError:
#         print('inputs must be numbers')
#     except Exception as e:
#         print(type(e))
#         print('an error occured')
#     finally:
#         print('Please visit us again.')





