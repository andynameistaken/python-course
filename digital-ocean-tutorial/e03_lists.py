def main():
    fish = ['barracuda', 'cod', 'devil ray', 'eel']
    print(fish)

    # append
    fish.append('flounder')
    print(fish)

    # insert
    fish.insert(1, 'tuna')
    print(fish)

    # extend
    more_fish = ['goby', 'herring', 'ide', 'kissing gourami']
    fish.extend(more_fish)
    print(fish)

    # list.remove
    fish.remove('kissing gourami')
    print(fish)

    # list.pop
    print(fish.pop(2))
    print(fish)

    # list.index('name')
    print(fish.index('tuna'))

    # list.copy()
    fish_2 = fish.copy()
    print('copy of fishes ', fish_2)

    # list.reverse()
    fish.reverse()
    print(fish)

    # list.count()
    print(fish.count('goby'))
    fish_ages = [1,2,4,3,2,1,1,2]
    print(fish_ages.count(1))

    # list.sort()
    fish_ages.sort()
    print(fish_ages)

    # list.clear()
    fish_2.clear()
    print(fish_2)

    # checking if something is in list
    letters = ['a', 'b', 'c', 'x']
    print('a' in letters)


if __name__ == '__main__':
    main()
