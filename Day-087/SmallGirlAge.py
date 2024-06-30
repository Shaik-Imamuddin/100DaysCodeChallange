#SmallGirlAge

#By using string Slicing
age=input()
print(int(age[:1]))    #Time Complexity:O(1)

#By using indexing
age=input()
print(int(age[0]))      #Time Complexity:O(1)

#By using looping statement
age=input()
for x in age:
    if x.isdigit():         #Time Complexity:O(n)
        print(int(x))

