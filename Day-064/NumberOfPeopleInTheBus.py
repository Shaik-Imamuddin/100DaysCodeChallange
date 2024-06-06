#NumberOfPeopleInTheBus

#By using for loop
bus_stops=[[10,0],[3,5],[5,8]]
count=0
for i in bus_stops:
    count+=i[0]-i[1]        #Time Complexity:O(n)
print(count)

#By using tuple comprehension
bus_stops=[[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]
print(sum(i-j for i,j in bus_stops))        #Time Complexity:O(n)

#By using list Comprehension
bus_stops=[[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]
print(sum([i[0]-i[1] for i in bus_stops]))      #Time Complexity:O(n)


#By using 2 for loops along with 2 variables(enter,exit)
bus_stops=[[3,2],[5,1],[15,5],[12,6],[6,8],[17,10]]
enter,exit=0,0
for i in bus_stops:
    enter=enter+i[0]        #Time Complexity:O(n)
for i in bus_stops:
    exit=exit+i[1]
res=enter-exit
print(res)
