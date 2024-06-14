#BasicMathematicalOperations

#By using Conditional stetements
value1=int(input())
value2=int(input())
operator=input()
if operator=='+':print(value1+value2)   #Time Complexity:O(1)
elif operator=='-':print(value1-value2)
elif operator=='*':print(value1*value2)
else:print(value1/value2)
print("--------------------------------")

#we can compress the above code By using Conditional stetementsin a single statement
value1=int(input())
value2=int(input())         #Time Complexity:O(1)
operator=input()
print(value1+value2 if operator=='+' else value1-value2 if operator=='-' else value1*value2 if operator=='*' else value1/value2)
print("--------------------------------")

#By using dictionaries along with operator key
value1=int(input())
value2=int(input())     #Time Complexity:O(1)
operator=input()
print({'+' : (value1 + value2),'-' : (value1 - value2),'*' : (value1 * value2),'/' : (value1 / value2)}[operator])
print("--------------------------------")

#By using dictionaries along with get() method
value1=int(input())
value2=int(input())     #Time Complexity:O(1)
operator=input()
print({'+':value1+value2,'-':value1-value2,'*':value1*value2,'/':value1/value2}.get(operator))
print("--------------------------------")

#By using eval method along with format string
value1=int(input())         
value2=int(input())     #Time Complexity:O(1)
operator=input()
print(eval(f'{value1}{operator}{value2}'))
print("--------------------------------")

#By using eval method along with format string
value1=int(input())
value2=int(input())         #Time Complexity:O(1)
operator=input()
print(eval(str(value1) + operator + str(value2)))
