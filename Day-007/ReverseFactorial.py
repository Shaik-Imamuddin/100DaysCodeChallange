#write a program that takes any number and returns
#The number that it is a factorial of input integer.
#So, if your function receives 120, it should return "5!" (as a string).


#By using loop
num=int(input("Enter a number:"))
fact=i=1
while True:
    fact=fact*i
    i+=1
    if fact==num:
        print(f"{i-1}!")        #Time Complexity : O(log num)
        break
    if fact>num:
        print('None')
        break

#we can compress the code  
num=int(input("Enter a number:"))
i = fact = 1
while fact < num:               #Time Complexity : O(log num)
    i += 1
    fact *= i
print('None') if fact > num else print("%d!"%i)
