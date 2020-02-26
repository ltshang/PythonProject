from random import randint

def play():
    random_int = randint(0,100)

    while True:
        user_guess = int(input('请输入你要猜的数字（0-100）'))

        if user_guess == random_int:
            print(f'you found the number ({random_int}),Congrats')
            break
        if user_guess < random_int:
          print('your number is less than the nubmber we guessed')
          continue
        if user_guess > random_int:
          print('your number is more than the nubmber we guessed')
          continue

if __name__ == '__main__':
    play()