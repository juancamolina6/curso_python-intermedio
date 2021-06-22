def run():
    lis = [1,2,3,4,5]

    #squared = [i**2 for i in range(1,len(lis)) ]
    squared = lis(map(lambda x: x**2, lis))
    print(squared)


if __name__ == '__mein__':
    run()
