#CombineStrings

#By using join() method
first=input()
last=input()                    #Time COmplexity:O(n)
print(" ".join([first,last]))

#By using format specifiers
first=input()
last=input()                #Time COmplexity:O(n)
print("%s %s"%(first,last))

#By using formatted string
first=input()
last=input()                #Time COmplexity:O(n)
print(f'{first} {last}')

#By using .format string
first=input()
last=input()                        #Time COmplexity:O(n)
print('{} {}'.format(first,last))

#By using string Conacatination
first=input()
last=input()            #Time COmplexity:O(n)
print(first+" "+last)
