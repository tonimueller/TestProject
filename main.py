from Animal import Animals

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(f'Get a new pet: ')
    frog = Animals('Froggy')
    frog.print_name()
    frog.set_size(10)
    frog.set_age(2)
    frog.print_size()
    frog.print_age()
    print (f'One year later...')
    frog.increment_age()
    frog.print_age()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
