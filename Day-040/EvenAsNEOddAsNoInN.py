#EvenOrOdd
#return all the even numbers in n as a number NE.
#return all the odd numbers in n as a number NO.

#By using join method along with list comprehension
N=int(input())
NE_digits = ''.join([digit for digit in str(N) if int(digit) % 2 == 0])
NE = int(NE_digits) if NE_digits else 0
    
NO_digits = ''.join([digit for digit in str(N) if int(digit) % 2 != 0])
NO = int(NO_digits) if NO_digits else 0
    
print(NE, NO)       #Time Complexity: O(n)


#By using string concatination
n=int(input())
lst = ['0','0']
for i in str(n):        #Time Complexity: O(n)
    if int(i)%2:
        lst[1] += i
    else:
        lst[0] += i
print(tuple(int(i) for i in lst))

#By using join method along with conditions
n=int(input())
ne = "".join(x for x in str(n) if x in "02468")     #Time Complexity: O(n)
no = "".join(y for y in str(n) if int(y) % 2)
print(tuple(0 if not a else int(a) for a in (ne, no)))

#By using conditional statements
n=int(input())
ne = ""
no = ""
for x in str(n):
    if int(x) % 2 == 0:             #Time Complexity: O(n)
        ne += x
    else:
        no += x
    if len(ne) == 0:
        ne = "0"
    if len(no) == 0:
        no = "0"
print((int(ne), int(no)))
