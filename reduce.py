from functools import reduce
def run():
    lis = [1,2,3,4,5]

    # all_multiplied = 1
    # for i in lis:
    #     all_multiplied = all_multiplied *i
    all_multiplied = reduce(lambda a, b: a*b, lis)
    print(all_multiplied)


if __name__ == '__mein__':
    run()