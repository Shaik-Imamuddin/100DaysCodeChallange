#ValidateThePin

#By using conditons.
pin=input()
if pin.isnumeric() and len(pin) in [4,6]:print(True)
else:print(False)       #Time Complexity:O(n)

#By using Nested if condition
pin=input()
if pin.isdigit():
    if(len(pin)==4 or len(pin)==6):print(True)
    else:print(False)       #Time Complexity:O(n)

#directly By using The print Statement along with len() and isdigit().
pin=input()
print(len(pin) in (4, 6) and pin.isdigit())     #Time Complexity:O(n)
