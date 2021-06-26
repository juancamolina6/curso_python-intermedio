def divisors(num):
    try:
        if num < 0:
            raise ValueError('No se puede ingresar Numeros negativos')
        divisor = [i for i in range(1,num+1) if num % i == 0]
        for i in divisor:
            print(i)
    except ValueError as ve:
        print(ve)
        return False

    # divisors = []
    # for i in range(1, num+1):
    #     if num % i == 1:
    #         divisors.append(i)
    # return divisors

def run():
    try:
        num = int(input("ingresa un numero: "))
        print(divisors(num))
        print("Termino mi programa")
    except ValueError:
        print("Dedes ingresar un numero")

if __name__ == '__main__':
    run()