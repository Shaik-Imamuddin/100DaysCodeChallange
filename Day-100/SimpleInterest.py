#Simple Interest

#By using formula of SI
p = int(input("Enter Principal Amount: "))
r = int(input("Enter Rate of Interest: "))
t = int(input("Enter Time Period in Months: "))     #Time Complexity:O(1)
si = (p*r*t)/100
print(f"Simple Interest is: {si}")


#By using Functions

def Cal_SI(p,r,t):
    return (p*r*t)/100
principal = int(input("Enter Principal Amount: "))
rate = int(input("Enter Rate of Interest: "))
time = int(input("Enter Time Period in Months: "))      #Time Complexity:O(1)

print(f"Simple Interest is: {Cal_SI(principal,rate,time)}")
