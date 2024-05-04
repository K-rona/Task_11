class EAN_13:
    country_codes = {}
    with open('Country_codes.txt', 'r', encoding='utf8') as f:
        code_info = f.readlines()
    for pair in code_info:
        number = pair.split()[0]
        country = pair.split()[1].rstrip()
        country_codes[country] = list(map(int, number.split('-')))

    goods_info = {}
    with open('123456.txt', 'r', encoding='utf8') as f:
        product_list = f.readlines()

    for element in product_list:
        number, info = element.split(':')
        goods_info[number] = info.rstrip().split(',')

    @staticmethod
    def get_info():
        for number, info in EAN_13.goods_info.items():
            print(number + " -", *info)
