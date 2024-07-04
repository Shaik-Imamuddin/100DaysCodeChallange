#VowelCount

#By using looping statement
sentence=input()
count=0
for i in sentence:
    if i in "aeiouAEIOU":       #Time Complexity:O(n)
        count+=1
print(count)

#By using tuple comprehension along with string
sentence=input()
print(sum(1 for let in sentence if let in "aeiouAEIOU"))    #Time Complexity:O(n)

#By using tuple comprehension along with list
sentence=input()
print(sum(sentence.count(char) for char in ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']))      #Time Complexity:O(n)

#By storing the value in a variable and incrementing it for each vowel
sentence=input()
c=0
c=c+sentence.count("A")
c=c+sentence.count("E")
c=c+sentence.count("I")     #Time Complexity:O(n)
c=c+sentence.count("O")
c=c+sentence.count("U")
c=c+sentence.count("a")
c=c+sentence.count("e")
c=c+sentence.count("o")
c=c+sentence.count("u")
c=c+sentence.count("i")
print(c)

