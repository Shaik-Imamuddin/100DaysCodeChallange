#WillYouMakeIt

#By using <= operator along with conditions
distance_to_pump=int(input())
mpg=int(input())
fuel_left=int(input())      #Time Complexity:O(1)
print(True if distance_to_pump/fuel_left<=mpg else False)
print("-------------------------------")

#By using <= operator
distance_to_pump=int(input())
mpg=int(input())
fuel_left=int(input())      #Time Complexity:O(1)
print(distance_to_pump <= mpg * fuel_left)
print("-------------------------------")

#By using >= operator
distance_to_pump=int(input())
mpg=int(input())
fuel_left=int(input())      #Time Complexity:O(1)
print(fuel_left >= distance_to_pump / mpg )
