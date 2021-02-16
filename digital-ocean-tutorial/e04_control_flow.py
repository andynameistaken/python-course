# if
if 4 > 6:
    print("not good")

if 4 < 6:
    print("better")

if 6 == 6:
    print("also ok")

if True:
    print("always will do")

if False:
    print("never gonna do")

#num = input('give me first number:  ')
#num1 = input("give me second number ")
#print(num, " ", num1)
#
##elif (else if)
#if num > num1:
#    print(num, " is bigger than ", num1)
#elif num < num1:
#    print(num, " is smaller than ", num1)
#else:
#   print(num, " equals ", num1) 
# while
numbers = []
i = 0

while i < 4:
    numbers += [i]
    i += 1

print(numbers)

for j in [4, 5, 6]:
    numbers += [j]
print(numbers)

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

#for loop & range()
print(range(5))
for i in range(5):
    print(i)
for i in range(0, 10 ,2): 
    print(i)

a = ['Monty', 'Python\'s', 'Flying', 'Circus' ]
for i in range(len(a)):
    print(i, a[i])


'''
enumerate(iterable, start=0)
Return an enumerate object. iterable must be a sequence, an iterator, or some other object which supports iteration. 
The __next__() method of the iterator returned by enumerate() returns a tuple containing a count (from start which 
defaults to 0) and the values obtained from iterating over iterable.
'''

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))
print(list(enumerate(seasons, start=1)))

# continue
for i in range (2, 10):
    if i % 2 == 0:
        print("Even number: ", i)
        continue
    print("Number: ", i)


# enumerate

