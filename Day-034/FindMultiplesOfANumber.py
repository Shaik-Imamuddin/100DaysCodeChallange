#FindMultiplesOfANumber

#By using list comprehension with condition
integer=int(input())
limit=int(input())      #Time Complexity: O(n)
print([i for i in range(1, limit+1) if i%integer == 0])


#By using list Comprehension only with loop
integer=int(input())
limit=int(input())      #Time Complexity: O(n)
print([i for i in range(integer, limit + 1, integer)])


#By using While loop along with append function
integer=int(input())
limit=int(input())
arr = []
count = integer
while count <= limit:       #Time Complexity: O(n)
    arr.append(count)
    count += integer
print(arr)

#By using list Method
integer=int(input())
limit=int(input())
print(list(range(integer, limit+1, integer)))   #Time Complexity: O(n)


#By using for loop along with append method
integer=int(input())
limit=int(input())
l=[]
for i in range(integer,limit+1):
    l.append(integer)
    integer+=l[0]       #Time Complexity: O(n)
    i+=integer
    if integer>=limit+1:
        break
print(l)
