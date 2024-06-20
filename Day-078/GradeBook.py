#GradeBook

#By using Conditional Statements
s1=int(input())
s2=int(input())
s3=int(input())
a=sum([s1,s2,s3])//3
if a>=90: print("A")            #Time Complexity:O(1)
elif a>=80 and a<90: print("B")
elif a>=70 and a<80: print("C")
elif a>=60 and a<70: print("D")
else:print("F")

Print("---------------------------------")

#We can compress the above code by writing conditions in print statement
s1=int(input())
s2=int(input())
s3=int(input())         #Time Complexity:O(1)
score =(s1+s2+s3)/3
print('A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'D' if score >= 60 else 'F')
