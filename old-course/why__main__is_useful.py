def do_stuff_on_import():  # Anything needed when the module is imported
    print('doing stuff on import')


def main():  # Stuff to do when run from the command line
    print('main funcion')


if __name__ == '__main__':
    main()
else:
    do_stuff_on_import()
