#HowOldWillIBeIn2099

#By using conditional statements.
year_of_birth=int(input())
current_year=int(input())
age=current_year-year_of_birth
if age > 0:
    if age == 1:
        print(f"You are {age} year old.")       #Time Complexity: O(1)
    else:
        print(f"You are {age} years old.")
elif age < 0:
    if abs(age) == 1:
        print(f"You will be born in {abs(age)} year.")
    else:
        print(f"You will be born in {abs(age)} years.")
else:
    print("You were born this very year!")


#We can compress the above code
year_of_birth=int(input())
current_year=int(input())           #Time Complexity: O(1)
if year_of_birth == current_year: print("You were born this very year!")
elif year_of_birth < current_year: print("You are 1 year old.") if current_year-year_of_birth== 1 else print(f'You are {current_year-year_of_birth} years old.')
else: print("You will be born in 1 year.") if year_of_birth-current_year == 1 else print(f'You will be born in {year_of_birth - current_year} years.')
