is_male = True
is_tall = True
if is_male or is_tall:
    print("you are a male or tall or both")
else:
    print("you are neither male or tall")

if is_male and is_tall:
    print("you are male and tall")
elif is_male and not(is_tall):
    print("you are male but not tall")
elif not(is_male) and not is_tall:
    print("you are female but not tall")
else:
    print("you are either not male or not tall ot both")



def max_num(num1, num2, num3):
    if(num1 >= num2 and num1 >= num3):
        return num1
    elif(num2>=num3 and num2 >= num1):
        return num2
    else:
        return num3

print(max_num(8932948,3984,230498))