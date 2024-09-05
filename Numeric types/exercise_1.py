#number guessing game
import random


def guessing_game():
    number = random.randint(0,100)
    #move input under while loop to keep asking user for guess
    #try and except removes unwanted inputs
    #using f-strings to format outputs

    while True:
        try:
            guess = int(input("enter your guess "))
            if guess < number:
                print(f'{guess} is low, try higher')
            elif guess > number:
                print(f'{guess} is high, try lower')
            else:
                break
        except ValueError:
            print("not a valid integer")

guessing_game()

'''
About module random
Python uses the Mersenne Twister as the core generator. It is deterministic in nature, thus not cryptographic safe.

random.seed(a=None, version=2)
initializes the random number generator, uses current system time if 'a' is omitted

random.randbytes(n)
generates 'n' random bytes. Don't use for generating security tokens. Use module secrets.

random.randrange(stop)
random.randrange(start, stop, step)
returns a random number from range(start, stop, step). Don't use keyword arguments as they are
interpted in unexpected ways.

random.randint(a,b)
returns a random integer N such that a<= N <= b

random.choice(sequence)
returns a random item from a non-empty 'sequence'. If sequence is empty, raises IndexError

random.choices(population, weights=None, *, cum_weights=None, k=1)
returns a k-sized list of elements from the 'population' with replacement
if weights sequence is supplied, selection are made on basis of relative weights
if cum_weights is supplied, selections are made on basis of it
TypeError if length of weights is not equal to population
ValueError if all weights are zero
IndexError if population is empty

random.shuffle(x)
shuffles the 'sequence' in place.

random.shuffle(x, k=len(x))
shuffles an immutable sequence and returns a new shuffled list

random.sample(population, k, *, counts=None)
returns a k length list of elements from population without replacement

random.binomialvariate(n=1, p=0.5
Binomial distribution. Returns the number of successes for 'n' independent trials with the probability of success of each being 0.5

random.random()
returns next floating-point number in the range 0.0 to 1.0

random.uniform(a,b)
returns a random floating point between a and b both inclusive.
'''