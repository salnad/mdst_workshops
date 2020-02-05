"""
MDST Workshop 1 - Python Basics Starter Code
"""

# Add any imports you need here:
import random
import base64

def part1(num):
    """
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate (i.e. "even" or "odd") message to the user.
    """
    if (num % 2 == 0):
        print('even')
    else:
        print('odd')

def part2():
    """
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user
    to guess the number, then tell them whether they guessed too low, too high,
    or exactly right.
    (Hint: remember to use the user input lessons from the very first
    exercise).
    Keep the game going until the user types "exit".
    [ try checking the random module in python on google. Concepts: Infinite
    loops, if, else, loops and user/input].
    """
    num = random.randint(1,9)
    guess = input('enter your guess: ')
    while True:
        if (guess == 'exit'):
            break
        elif (num > int(guess)):
            print('your guess is to low')
        elif (num < int(guess)):
            print('your guess is to high')
        else:
            print('your guess is just right')
        guess = input('enter your guess: ')
        

def part3(string):
    """
    Ask the user for a string and print out whether this string is a palindrome
    or not. (A palindrome is a string that reads the same forwards and
    backwards.)
    """
    n = len(string)
    front = 0
    back = n-1
    while (front < back):
        if (string[front] != string[back]):
            print('not a palindrome')
            return
        front += 1
        back -= 1
    print('is a palindrome')


def part4a(filename, username, password):
    """
    Encrypt your username and password using base64 module
    Store your encrypted username on the first line and your encrypted password
    on the second line.
    """
    user_encode = base64.b64encode(username.encode('utf-8'))
    pword_encode = base64.b64encode(password.encode('utf-8'))

    with open(filename,'w+') as file:
        file.write(str(user_encode))
        file.write('\n')
        file.write(str(pword_encode))

def part4b(filename, password=None):
    """
    Create a function to read the file with your login information.
    Print out the decrypted username and password.
    If a password is specified, update the file with the new password.
    """
    with open(filename,'r') as file:
        username = file.readline()
        password = file.readline()
        print(str(base64.b64decode(username)))
        # print(password)


if __name__ == "__main__":
    # part1(3)  # odd!
    # part1(4)  # even!
    # part2()
    # part3("ratrace")  # False
    # part3("racecar")  # True
    part4a("secret.txt", "naitian", "p4ssw0rd")
    part4b("secret.txt")
    #part4b("secret.txt", password="p4ssw0rd!")
    #part4b("secret.txt")
