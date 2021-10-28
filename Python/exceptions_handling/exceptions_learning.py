while True:
    try:
        my_input = int(input("Enter value for a number: "))
    except ValueError:
        print('Not a valid input because input is not int')
    else:
        print('Runs only when try is run')
        break
    finally:
        print('Runs no matter what')
