#TheFeastOfManyBeasts

#By using string indexing and double equal operator
beast=input()
dish=input()            #Time Complexity:O(1)
print([beast[0], beast[-1]] == [dish[0], dish[-1]])

#By using startswith() and endswith() methods
beast=input()
dish=input()        #Time Complexity:O(1)
print(beast.startswith(dish[0]) and beast.endswith(dish[-1]))

#By using string indexing along with and operator
beast=input()
dish=input()        #Time Complexity:O(1)
print(beast[0]==dish[0] and dish[-1]==beast[-1])
