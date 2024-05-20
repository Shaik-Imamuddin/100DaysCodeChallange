#calculate BMI

#By using split() method()
weight=int(input())
height=float(input())               #Time Complexity:O(1)
result = weight / height / height
print("Underweight Normal Overweight Obese".split()[(result > 18.5) +(result > 25.0) +(result > 30.0)])

#By using conditional statements
weight=int(input())
height=float(input())
bmi=weight/(height**2)
if bmi<=18.5: print("Underweight")
elif bmi<=25.0: print("Normal")               #Time Complexity:O(1)
elif bmi<=30.0: print("Overweight")
else: print("Obese")

#We can compress the code the By writing all the conditions in print statements
weight=int(input())
height=float(input())
bmi = weight / height ** 2
print('Underweight' if bmi <= 18.5 else 'Normal' if bmi <= 25.0 else 'Overweight' if bmi <= 30.0 else "Obese")      #Time Complexity:O(1)

#By using list indexing
weight=int(input())
height=float(input())
b = weight / height ** 2
print(['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)])       #Time Complexity:O(1)
