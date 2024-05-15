#Creating Dictionary By using Two Lists

#By using fromkeys and zip method
n=int(input())
keys=[]
for i in range(n):
    i=input()
    keys.append(i)
print(keys)
m=int(input())
values=[]
for i in range(m):
    i=int(input())
    values.append(i)
print(values)                       #Time Complexity:O(n)
keys_vals = dict.fromkeys(keys)
for key, val in zip(keys, values):
    keys_vals[key] = val
print(keys_vals)


#We can compress the above code by using or operator
n=int(input())
keys=[]
for i in range(n):
    i=input()
    keys.append(i)
print(keys)
m=int(input())
values=[]
for i in range(m):
    i=int(input())
    values.append(i)        #Time Complexity:O(n)
print(values)
print(dict.fromkeys(keys) | dict(zip(keys,values)))

#By using zip method along with while loop
n=int(input())
keys=[]
for i in range(n):
    i=input()
    keys.append(i)
print(keys)
m=int(input())
values=[]
for i in range(m):
    i=int(input())
    values.append(i)            #Time Complexity:O(min(n, m)).
print(values)
while len(keys) > len(values):
    values.append(None)
dic = dict(zip(keys, values))
print(dic)


#By using Dictionary comprehension

n=int(input())
keys=[]
for i in range(n):
    i=input()
    keys.append(i)
print(keys)
m=int(input())
values=[]
for i in range(m):
    i=int(input())
    values.append(i)        #Time Complexity:O(min(n, m)).
print(values)
print({k: v for k, v in zip(keys, values)} if len(keys) <= len(values) else {k: v for k, v in zip(keys, values)} | {k: None for k in keys[len(values):]})
