from random import randint
import sys

answer = randint(int(sys.argv[1]), int(sys.argv[2]))
guess_try = 0

print('''
AHOY! I\'m the Dread Pirate Roberts, and I have a secret!
Hint: It is a number between {}~{}. Best of luck matey!
I give you 8 tries 
'''.format(sys.argv[1], sys.argv[2]))

print('The answer:')
print(answer)

while True:
    try:
        guess = int(input('guess a number {}~{}:  '.format(sys.argv[1], sys.argv[2])))
        plus_minus = guess // 10

        if guess_try < 8:
            if int(sys.argv[1]) < guess < int(sys.argv[2])+1:
                guess_try += 1

                if guess == answer:
                    print('Avast! Ye got it! Found my secret, ye did!')
                    break
                elif (guess < (answer + plus_minus)) and (guess > answer):
                    print('High, landlubber!')
                elif guess > (answer + plus_minus-1):
                    print('Too high, landlubber!')
                elif (guess > (answer - plus_minus)) and (guess < answer):
                    print('Low, ye scruwy dog!')
                elif guess < (answer - plus_minus+1):
                    print('Too low, ye scurvy dog!')

            else:
                print('hey bozo, I said {}~{}'.format(sys.argv[1], sys.argv[2]))

        else:
            print('No more guesses! Better luck next time, matey!')
            print('The secret number was {}'.format(answer))
            quit()
    except ValueError:
        print('please enter a number')
        continue

print('Thankyou...')
print('Bye...')
