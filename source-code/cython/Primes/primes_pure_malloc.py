import cython
from cython.cimports.libc.stdlib import malloc, free

def primes(nb_primes: cython.int):
    i: cython.int
    p: cython.p_int = cython.cast(cython.p_int, malloc(nb_primes*cython.sizeof(cython.int)))


    len_p: cython.int = 0  # The current number of elements in p.
    n: cython.int = 2
    while len_p < nb_primes:
        # Is n prime?
        for i in p[:len_p]:
            if n % i == 0:
                break

        # If no break occurred in the loop, we have a prime.
        else:
            p[len_p] = n
            len_p += 1
        n += 1

    # Let's copy the result into a Python list:
    result_as_list = [prime for prime in p[:len_p]]
    free(p)
    return result_as_list
