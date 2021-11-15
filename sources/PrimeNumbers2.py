from math import sqrt

## change_test
def prime_numbers(natural_number_input):
    """
    :param natural_number_input: natural number.
    :return: Amount of prime numbers smaller than this natural number.
    """
    list_of_prime_numbers = [2]
    for natural_number in range(3, natural_number_input + 1, 2):

        is_prime = True
        for b in range(3, int(sqrt(natural_number)) + 1, 2):
            c = natural_number % b
            if c == 0:
                is_prime = False
                break
        if is_prime:
            list_of_prime_numbers.append(natural_number)
    return list_of_prime_numbers


def n_of_prime_numbers(natural_number_input):
    return len(prime_numbers(natural_number_input))
