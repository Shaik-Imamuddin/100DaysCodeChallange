#CatYearsDogYears

#By using Conditional Statements.
human_years=int(input())
if human_years == 1:
    cat_years = dog_years = 15
elif human_years == 2:                  #Time Complexity: O(1)
    cat_years = dog_years = 24
else:
    cat_years = 4 * human_years + 16
    dog_years = 5 * human_years + 14
print([human_years,cat_years,dog_years])

print("-----------------------------------")

#Only By using Operators
human_years=int(input())
cat_years = 15 + (9 * (human_years > 1)) + (4 * (human_years - 2) * (human_years > 2))
dog_years = 15 + (9 * (human_years > 1)) + (5 * (human_years - 2) * (human_years > 2))
print([human_years,cat_years,dog_years])        #Time Complexity: O(1)

print("-----------------------------------")
#By Using Nested Conditions.
human_years=int(input())
dog_years,cat_years=0,0
if human_years>=1:
    if human_years==1:
        dog_years+=15
        cat_years+=15
    elif human_years==2:        #Time Complexity: O(1)
        dog_years+=24
        cat_years+=24
    else:
        dog_years+=(15+9+((human_years-2)*5))
        cat_years+=(15+9+((human_years-2)*4))
print([human_years,cat_years,dog_years])
print("-----------------------------------")
