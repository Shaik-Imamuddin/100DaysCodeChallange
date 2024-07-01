#AreYouPlayingBanjo

#By using conditions along with string indexing
name=input()        #Time Complexity:O(1)
print(name + " plays banjo" if name[0].lower() == 'r' else name + " does not play banjo") 


#By using conditions along with startswith() method 
name=input()
if name.startswith('R'): print(name+" plays banjo")
elif name.startswith('r'): print(name+" plays banjo")       #Time Complexity:O(1)
else: print(name+" does not play banjo")
