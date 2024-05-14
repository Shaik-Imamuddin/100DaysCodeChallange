#Mumbling

#By using string Concatnation
s=input()
i = 0
result = ''
for letter in s:
    result += letter.upper() + letter.lower() * i + '-'
    i += 1
print(result[:len(result)-1])       #Time Complexity:O(n^2)

#By using string Concatnation along with title method.
s=input()
output = ""
for i in range(len(s)):
    output+=(s[i]*(i+1))+"-"
print(output.title()[:-1])      #Time Complexity:O(n^2)

#By using tuple comprehension
s=input()       #Time Complexity:O(n)
print('-'.join(c.upper() + c.lower() * i for i, c in enumerate(s)))

#By using List Comprehension
s=input()       #Time Complexity:O(n)
print("-".join([str(s[i] * (i + 1)).capitalize() for i in range(len(s))]))
