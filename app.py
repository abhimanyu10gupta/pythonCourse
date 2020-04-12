try:
    number = 10/0
    number1 = int(input("enter your number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invalid input")