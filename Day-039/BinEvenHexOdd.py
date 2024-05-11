#EvenOrOdd
#If Even return Binary  number
#if odd return Hexa-decimal number

#By using conditional statements
n=int(input())
if n % 2 == 0:
    print(bin(n).removeprefix("0b"))
else:
    print(hex(n).removeprefix("0x"))    #Time Complexity :O(log n)

#By compressing the code by using conditional statements
n=int(input())
print(bin(n)[2:] if n%2==0 else hex(n)[2:])     #Time Complexity :O(log n)


#By using list comprehension along with conditions
n=int(input())
print([hex(n),bin(n)][n%2==0][2:]) #Time Complexity :O(1)


#By using format specifiers
n=int(input())
print(format(n,('x' if n%2 else 'b')))  #Time Complexity :O(1)
