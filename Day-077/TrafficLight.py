#TrafficLight

#By using Dictionaries
current=input()         #Time Complexity:O(1)
print( {"green": "yellow", "yellow": "red", "red": "green"}[current])

print("-------------------------------")

#By using Conditional statements
current=input()
if current=='green': print( 'yellow')       #Time Complexity:O(1)
elif current=='yellow': print( 'red')
else:print( 'green')
