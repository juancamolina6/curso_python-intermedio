def run():
    lis = [1,2,3,4,5]

    #odd = [i for i in lis if i%2 != 0]
    odd = list(filter(lambda x: x%2 != 0, lis))
    print(odd)


if __name__ == '__mein__':
    run()