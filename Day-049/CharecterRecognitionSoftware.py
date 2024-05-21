#CharacterRecognitionSoftware

#By using loop along with replace() method.
s=input()
for i in s:
    s=s.replace("5","S")    #Time Complexity:O(n^2)
    s=s.replace("0","O")
    s=s.replace("1","I")
print(s)

#We can directly use the replace() method in print ststement.
s=input()       #Time Complexity:O(n)
print(s.replace('1','I').replace('0','O').replace('5','S'))
