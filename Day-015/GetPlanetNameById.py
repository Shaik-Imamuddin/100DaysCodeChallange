#GetPlanetNameById
#Write a program to print the planet name based on the given id.

#By using lists
id=int(input())
list=[None,"Mercury","Venus", "Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]
print(list[id])         #Time Complexity: O(1)
print("-----------------------------")

#By using Match case
id=int(input())
name=""
match id:
    case 1: name = "Mercury"
    case 2: name = "Venus"
    case 3: name = "Earth"
    case 4: name = "Mars"
    case 5: name = "Jupiter"
    case 6: name = "Saturn"
    case 7: name = "Uranus"  
    case 8: name = "Neptune"
print(name)                     #Time Complexity: O(1)
print("-----------------------------")

#By using Dictionaries
id=int(input())
planets = {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus", 
        8: "Neptune",
    }
print(planets[id])          #Time Complexity: O(1)
print("-----------------------------")

#By using dictionaries along with get() method
id=int(input())
print({
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune",
    }.get(id, None))            #Time Complexity: O(1)
