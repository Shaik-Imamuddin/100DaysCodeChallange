#OppositesAttract

#By using Conditional operators
flower1=int(input())
flower2=int(input())
if flower1%2==0 and flower2%2==0:       #Time Complexity:O(1)
    print(False)
elif flower1%2==0 or flower2%2==0:
    print(True)
else:print(False)

#By using double equalto operator
flower1=int(input())
flower2=int(input())                    #Time Complexity:O(1)
print((flower1 + flower2) % 2 == 1)

#By using not equalto operator
flower1=int(input())
flower2=int(input())                    #Time Complexity:O(1)
print(flower1%2 != flower2%2)
