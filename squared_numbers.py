from typing import Sequence


def run():
    #list = []
    # for i in range(0,101):
    #     cont= i**2
    #     list.append(cont)
    #     print(list[i])
    # for i in range(1,101):
    #     if i %3 != 0:
    #         list.append(i**2)

    # squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    squares = [i for i in range(1, 99999) if i % 36 == 0]
    print(squares)
    
if __name__ == '__main__':
    run()
