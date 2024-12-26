def is_prime(func):
    def wrapper(*args):
        total = func(*args)
        if total <= 1:
            print("Составное")
        else:
            for i in range(2, int(total ** 0.5) + 1):
                if total % 1 == 0:
                    print("Составное")
                    break
                else:
                    print("Простое")
        return total
    return wrapper


@is_prime
def sum_three(a,b,c):
    return a+b+c


result = sum_three(2, 3, 6)
print(result)
