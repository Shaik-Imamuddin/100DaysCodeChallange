#SquareEveryDigit

#By using String concatination
num=input()
sum=''
for i in str(num):      #Time Complexity:O(n^2)
    n=int(i)**2
    sum+=str(n)
print(int(sum))

#we can compress one line of code by using String concatination
num=input()
res = ""
for x in str(num):
    res += str(int(x)**2)   #Time Complexity:O(n^2)
print(int(res))

#By using list comprehension
num=input()
digits = [int(x) for x in str(num)]
print(int(''.join([str(x*x) for x in digits])))     #Time Complexity:O(n)

#By using list comprehension along with map function
num=input()
print(int(''.join([str(i * i) for i in map(int, str(num))])))       #Time Complexity:O(n)

#By using join method along with pow method
num=input()
print(int("".join(str(pow(int(i), 2)) for i in str(num))))      #Time Complexity:O(n)

#By using join method
num=input()
print(int(''.join(str(int(d)**2) for d in str(num))))       #Time Complexity:O(n)
