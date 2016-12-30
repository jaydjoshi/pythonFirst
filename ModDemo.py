'''
print odd and even numbers
'''

evenList = []
oddList = []

for n in range(101):
    if n % 2 is 0:
        evenList.append(n)
    else:
        oddList.append(n)

print("----------Even number----------")
for n in evenList:
    print(n)

print("----------Odd number----------")
for n in oddList:
    print(n)

