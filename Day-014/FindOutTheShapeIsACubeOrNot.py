#FindOutTheShapeIsACubeOrNot

#Write a Program

#To find the volume (centimeters cubed) of a cuboid you use the formula:
#volume = Length * Width * Height

#But someone forgot to use proper record keeping, so we only have the volume, and the length of a single side!
#It's up to you to find out whether the cuboid has equal sides (= is a cube).

#Return true if the cuboid could have equal sides, return false otherwise.
#Return false for invalid numbers too (e.g volume or side is less than or equal to 0).
#Note: side will be an integer

#By using The conditional statements
side,volume=int(input()),int(input())
if side>0 and volume>0:     
    print(True if side*side*side==volume else False)    #Time Complexity: O(1)
else:
    print(False)

#we can compress the code by using the conditions directly in print statement
print("---------------------------------")
side,volume=int(input()),int(input())
print(side > 0 and side ** 3 == volume) #Time Complexity: O(1)

#This is another condition to check the shape is cube or Not
print("---------------------------------")
side,volume=int(input()),int(input())
print(0 < volume == side**3)    #Time Complexity: O(1)
