
def fibbonaci(n):
    a = 0
    b = 1
    for i in range(1,n):
        temp = b
        b = b + a
        a = temp
    return b

def count_occurences(n, d):
    count = 0
    while(n>0):
        temp = n % 10
        if temp == d:
            count+=1
        n = int(n/10)
    return count


def reverse(n):
    reversed_digit = 0
    while(n>0):
        d = n % 10
        reversed_digit = reversed_digit*10 + d
        n = int(n/10)
    return reversed_digit

def is_prime(n):
    if n<=1:
        return False
    c = 2
    while(c*c<=n):
        if n%c == 0:
            return False
        else:
            c+=1
    return True
