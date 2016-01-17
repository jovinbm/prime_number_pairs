import util
import time
import sys


def get_user_input_int(question_string, start_inclusive, end_inclusive, default):
    try:
        user_input = int(raw_input(question_string))
    except:
        user_input = default

    if start_inclusive <= user_input <= end_inclusive:
        return user_input
    else:
        return default


def get_user_input_str(question_string, default):
    try:
        user_input = str(raw_input(question_string))
    except:
        user_input = default
    return user_input


class PRIME:
    def __init__(self):
        self.id = 'prime_pair_generator'
        print 'Welcome to prime number pairs generator'
        time.sleep(1)

        # limits

        print ''
        print 'Please specify the limits of the prime numbers to generate'
        while 1:
            self.prime_number_start = get_user_input_int(
                    "On which number should I start to look for prime numbers? (Integers from 0 to 99999, "
                    "Default = 0 for None or non-integer): ",
                    0,
                    99999,
                    0)

            self.prime_number_end = get_user_input_int(
                    "Where should I end? (Integers from 0 to 99999,"
                    " Default = 9999 for None or non-integer): ",
                    0,
                    99999,
                    0)

            if self.prime_number_start >= self.prime_number_end:
                print 'Oops, the start can not be greater or equal to the end. Please specify new limits'
            else:
                break

        # fix start of prime numbers to be 2 if less than 2, because that's where we know prime numbers start from
        if self.prime_number_start < 2:
            self.prime_number_start = 2

            if self.prime_number_end < self.prime_number_start:
                self.prime_number_end = 2

        # generate

        print ''
        print 'Okay, let me generate the prime numbers, this might take some time for wider ranges'
        print ''
        self.printThePrimeNumbers = [False, True][get_user_input_int(
                "Should I print the prime numbers that I've found? (1)YES or (0)NO? (0 or 1 only, "
                "Default = 0(NO) for None or non-integer): ",
                0,
                1,
                0)]

        self.prime_numbers = []
        self.find_prime_numbers()

        if self.printThePrimeNumbers:
            print ''
            print self.prime_numbers

        # find pairs?

        print ''
        self.find_pairs = [False, True][get_user_input_int(
                "Do you want to find prime number pairs? (1)YES or (0)NO? (0 or 1 only, "
                "Default = 0(NO) for None or non-integer): ",
                0,
                1,
                0)]
        if not self.find_pairs:
            print ''
            sys.exit('Bye')

        # powers of what?

        print ''
        self.base = get_user_input_int(
                "The difference between the pairs should be powers of (i.e base)? (2 to 1000 only, "
                "Default = 2 for None, non-integer or less than 2): ",
                2,
                1000,
                0)

        print ''
        self.index_limit = get_user_input_int(
                "Highest number to raise the base to (i.e index)? (1 to 100 only, "
                "Default = 1 for None, non-integer or less than 2): ",
                2,
                100,
                0)

        self.powers = [self.base ** j for j in range(1, self.index_limit + 1)]
        print ''
        print "I'll check the difference against the following powers: "
        time.sleep(1)
        print ''
        print self.powers

        # pairs
        print ''
        print 'Looking for the pairs...'
        self.prime_number_pairs = []
        self.find_prime_number_pairs()
        time.sleep(3)
        if len(self.prime_number_pairs) == 0:
            print ''
            print "I could not find any"
        else:
            print ''
            print "I found the following"
            print self.prime_number_pairs

    def find_prime_numbers(self):
        for itself in range(self.prime_number_start, self.prime_number_end):
            isPrime = True

            for divisor in range(self.prime_number_start, itself):
                if (itself % divisor) == 0:
                    isPrime = False
                    break

            if isPrime:
                self.prime_numbers.append(itself)

        return True

    def find_prime_number_pairs(self):
        for index, prime in enumerate(self.prime_numbers):
            for i in range(0, index):
                other_prime = self.prime_numbers[i]
                if (prime - other_prime) in self.powers:
                    self.prime_number_pairs.append((prime, other_prime))

        return True


P = PRIME()