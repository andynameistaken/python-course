
def spammer(bag=[]):
    print(spammer.__defaults__)
    bag.append("spam")
    print(spammer.__defaults__)
    print(len(spammer.__defaults__))
    
    return bag


spammer()

a = 1
b = 2
c = 3
print(a)

a, b, c = c, b, a
a