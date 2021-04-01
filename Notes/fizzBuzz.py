def fizzbuzz(a=15, b=3, c=5):

    for i in range(1, a + 1):

        if i % b == 0 and i % c == 0:
            print('FizzBuzz')

        elif i % b == 0:
            print('Fizz')

        elif i % c == 0:
            print('Buzz')

        else:
            print(i)


fizzbuzz()
