def is_prime_number(n):
     is_prime = True
     for i in range(2, n):
          if n % i == 0:
               is_prime = False
     return is_prime

print(is_prime_number(137))
