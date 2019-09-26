from math import factorial as fact

def get_coef(num):
    output = list()
    for i in range(num + 1):
        output.append(n_choose_r(num, i))
    return output

def n_choose_r(n, r):
    return fact(n)/(fact(r) * fact(n - r))

def main():
    n = 0
    while(n >= 0):
        n = int(input('Enter a number: '))
        print(get_coef(n))

if __name__ == '__main__':
    main()
