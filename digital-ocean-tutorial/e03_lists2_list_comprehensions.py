def main():
    shark_letters = [i for i in 'shark']
    print(shark_letters)

    number_list = [x ** 2 for x in range(10) if x % 2 == 0]
    print(number_list)

    my_list = []

    for x in [20, 40, 60]:
        for y in [2, 4, 6]:
            my_list.append(x * y)

    print(my_list)

    my_list = [x * y for x in [20, 40, 60] for y in [2, 4, 6]]
    print(my_list)

if __name__ == '__main__':
    main()