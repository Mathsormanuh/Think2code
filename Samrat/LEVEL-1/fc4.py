def palin():
    n=input('Enter the number.\n')
    rev=n[::-1]
    if n==rev:
        print('The number is a palindrome.\n')
    else:
        print('The number is not a palindrome.\n')
palin()