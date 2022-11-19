def is_prime(n):
    if n == 1:
        return False

    for divisor_candidate in range(2, n):
        if n % divisor_candidate == 0:
            return False
    else:
        return True

if __name__ == '__main__':
    print('running tests')
    if is_prime(1) != False:
        print('so a schas')
    if is_prime(2) != True:
        print('so a schas')
    if is_prime(28) != False:
        print('so a schas')
    
