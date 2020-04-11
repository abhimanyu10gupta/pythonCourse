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