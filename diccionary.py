import math
def run():
    # dicti = {}

    # for i in range(1, 101):
    #     if i%3 != 0:
    #         dicti[i] = i**3

    # print(dicti)
    # my_dict = {i: i**3 for i in range(1, 100) if i % 3 != 0}
    # print(my_dict)    
    my_dict = {i: math.sqrt(i) for i in range(1, 100) if i % 3 != 0}
    print(my_dict) 

if __name__ == '__main__':
    run()