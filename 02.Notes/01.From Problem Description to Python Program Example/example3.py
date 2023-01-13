while True:    
    print("1. Multiply the given number by 1 to 12")
    print('2. Sum two given numbers')
    print('3. Exit')
    choice = input('Please enter your choice: ')
    if choice == '1':
        num = float(input('Give a number: '))
        i = 1
        while i <= 12:
            print(num*i,end=' ') # use print(num*i) if we want to display one per line
            i = i + 1
        print()
    elif choice == '2':
        num1 = float(input('Give your first number: '))
        num2 = float(input('Give your second number: '))
        res = num1 + num2
        print(res)
    elif choice == '3':
        print("Goodbye")
        break
    else:
        print("Invalid choice")
