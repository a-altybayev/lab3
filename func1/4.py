def prime(num):
    for i in range(2, int(num ** 0.5)+1):
        if num%i == 0:
            return False
    return True
def filter_prime(number):
    return [num for num in number if prime(num)]
print(filter_prime([1, 12, 13, 3, 10, 2, 7, 9]))