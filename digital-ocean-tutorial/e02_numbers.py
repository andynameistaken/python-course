print("Numbers")
print('classic division returns a float: 15/2  = ', 15/2)
print('floor division ("//") discards the fractional part: 15//2 = ', 15 // 2)
print('modulo - remainder("%")| 15//2, remainder =  15 % 2)', 15//2, 'remainder = ', 15 % 2)
print('power ("**") 2**3 = ', 2**3)

print("\nStrings")
word = 'Dogs'
# word[0] = 'd' can't do Strings are immutable!
print(word)
print("word = 'Dogs")
print('len(word) = ', len(word))
print("string index word[index]")
print('word[0], word[1], word[2], word[3]')
print(word[0], word[1], word[2], word[3])
print('word[-1], word[-2], word[-3], word[-4]')
print(word[-1], word[-2], word[-3], word[-4])
print('word[-1], word[-2], word[-3], word[-0]')
print(word[-1], word[-2], word[-3], word[-0])

print('\nSlices')
print((word[:2]))
print(word[1:])
print(word[1:3])

print("\nLists")
numbers = [1, 2, 3, 4]
print(numbers)
numbers += [5, 6, 7,  8]
print(numbers)
numbers[0] = 0
print(numbers)
numbers.append(numbers[len(numbers) - 1] + 1)
print(numbers)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
numbers_and_letters = [numbers, letters]
print(numbers_and_letters)
print(numbers_and_letters[0])
print(numbers_and_letters[1])
print(numbers_and_letters[0][1])
print(numbers_and_letters[1][0])

