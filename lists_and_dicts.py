def  run():
    my_list = [1 , "Hello",True, 4.5]
    my_dict = {"firstname":"Desiy","lasname": "Guisa"}

    super_list = [
        {"firstname":"Desiy","lasname": "Guisa"},
        {"firstname":"Camilo","lasname": "Molina"},
        {"firstname":"Maria","lasname": "Rodrigues "},
        {"firstname":"Alejandor","lasname": "Restrepo"},
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,0,1,2],
        "floating_num": [1.1,4.5,6.45]
    }


    for key, value in super_dict.items():
        print(key, "-", value)


    # for key, in super_list:
    #     print(key.items())

    for values in super_list:
        for key, value in values.items():
            print(f'{key} - {value}')



if __name__ == '__main__':
    run()