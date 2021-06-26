def divisors(num):
        divisor = [i for i in range(1,num+1) if num % i == 0]
        for i in divisor:
            print(i)

def run():
        num = input("ingresa un numero: ")
        assert num.isnumeric(), "No debes ingresar letras o numeros negativos"
        print(divisors(int(num)))
        print("Termino mi programa")

if __name__ == '__main__':
    run()