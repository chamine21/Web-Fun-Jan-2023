for i in range(1, 151):
    print(i)
    
for i in range(5, 1001, 5):
    print(i)

for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

sum = 0
for i in range(1, 500001, 2):
    sum += i
print(sum)

i = 2018
while i > 0:
    print(i)
    i -= 4
    
lowI = 2
highI = 9
mult = 3

for i in range(lowI, highI + 1):
    if i % mult == 0:
        print(i)

