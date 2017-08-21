number = 23
running = True

while running:
    guess = int(input('Enter an integer : '))

    if guess == number:
        print('等于')
        running = False
    elif guess < number:
        print('小于')
    else:
        print('大于')
else:
    print('循环结束')

print('Done')