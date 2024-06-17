#SentenceSmash

#By using join() method along with conditions
words=[]
n=int(input())
for i in range(n):
    i=input()
    words.append(i)     #Time Complexity:O(n)
print(words)
if len(words) == 0:
    print('')
else:
    print(' '.join(words))

#we can compress the code by using join() method along with conditions
words=[]
n=int(input())
for i in range(n):
    i=input()
    words.append(i)     #Time Complexity:O(n)
print(words)
print(" ".join(words) if len(words)>0 else "")

#By using string concatination
words=[]
n=int(input())
for i in range(n):
    i=input()
    words.append(i)
s=""
for i in range(len(words)):
    if i<len(words)-1:
        s+=words[i]+" "     #Time Complexity:O(n^2)
    else:
        s+=words[i]
print(words)
print(s)

#only By using join() method
words=[]
n=int(input())
for i in range(n):
    i=input()
    words.append(i)     #Time Complexity:O(n)
print(words)
print(' '.join(words))
