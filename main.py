import random
end = ""
while end != "END".upper():
    computer_sign = random.choice(['STONE', 'PAPER', 'SCISSOR'])
    user_sign = input('Enter your sign: ')
    if user_sign.upper() == computer_sign:
        print("It's a draw")
        end = input('Press a key to continue: ')

    elif user_sign.upper() == "STONE" and computer_sign == "PAPER":
        print("You lose")
        end = input('Press a key to continue: ')

    elif user_sign.upper() == "STONE" and computer_sign == "SCISSOR":
        print("You Win")
        end = input('Press a key to continue: ')

    elif user_sign.upper() == "PAPER" and computer_sign == "SCISSOR":
        print("You lose")
        end = input('Press a key to continue: ')

    elif user_sign.upper() == "PAPER" and computer_sign == "STONE":
        print("You Win")
        end = input('Press a key to continue: ')

    elif user_sign.upper() == "SCISSOR" and computer_sign == "STONE":
        print("You lose")

        end = input('Press a key to continue: ')
    elif user_sign.upper() == "SCISSOR" and computer_sign == "PAPER":
        print("You Win")
        end = input('Press a key to continue: ')











