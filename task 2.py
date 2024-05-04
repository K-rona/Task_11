import Barcode


class Goods:
    def __init__(self, barcode: str):
        self.__barcode = barcode
        self.__producer = barcode[3:9]
        self.__product_number = barcode[9:12]
        for country, code in Barcode.EAN_13.country_codes.items():
            if len(code) == 2:
                if code[0] <= int(self.__barcode[:3]) <= code[1]:
                    self.country = country
            elif len(code) == 1:
                if self.__barcode[:3] == code:
                    self.country = country
        for number, info in Barcode.EAN_13.goods_info.items():
            if self.__product_number == number:
                self.__price = int(info[0])
                self.category = info[1]
                self.__name = info[2]
    price = property()
    name = property()
    barcode = property()

    @barcode.setter
    def barcode(self, value):
        pass

    @barcode.getter
    def barcode(self):
        return self.__barcode

    @price.setter
    def price(self, value):
        pass

    @price.getter
    def price(self):
        return self.__price

    @name.setter
    def name(self, value):
        pass

    @name.getter
    def name(self):
        return self.__name

    def __repr__(self):
        return f'Товар {self.__name} категории {self.category}, цена - {self.__price}'


class ShoppingCart:

    def __init__(self):
        self.__cart = []
    cart = property()

    @cart.setter
    def cart(self, value):
        pass

    @cart.getter
    def cart(self):
        return self.__cart

    def check_fill(self):
        return len(self.__cart) > 0

    def full_price(self):
        price = 0
        if self.check_fill:
            for element in self.__cart:
                price += element[2]
        return price

    @staticmethod
    def check_barcode(barcode: str):
        if len(barcode) == 13:
            main_body = barcode[:12]
            even_sum = 0
            odd_sum = 0
            for i in range(1, len(main_body), 2):
                even_sum += int(main_body[i])
            for j in range(0, len(main_body), 2):
                odd_sum += int(main_body[j])
            summ = even_sum * 3 + odd_sum
            for number in range(1000, 0, -10):
                if 0 <= number - summ <= 10:
                    contr_number = number - summ
                    if contr_number == int(barcode[-1:]):
                        return True
                    return False
        return False

    def add_good(self, barcode):
        if ShoppingCart.check_barcode(barcode):
            new_good = Goods(barcode)
            self.__cart += [[new_good.name, new_good.category, new_good.price, new_good.barcode]]
            return f'{new_good} добавлен в корзину.'
        return "Ошибка штрих-кода."

    def delete_good(self, barcode):
        if ShoppingCart.check_barcode(barcode):
            for element in self.__cart:
                if barcode in element:
                    self.__cart.remove(element)
                    return "Товар удален."
            return "Товара нет в корзине."
        return "Ошибка штрих-кода."

    def making_order(self):
        if self.check_fill():
            with open('Order.txt', 'w', encoding='utf8') as f:
                for element in self.__cart:
                    for info in element:
                        f.write(str(info) + " ")
                    f.write("\n")
                f.write("Общая стоимость: " + str(self.full_price()))
            return True
        else:
            return False


MENU = "1. Посмотреть список доступных товаров\n"\
       "2. Оформить заказ\n" \
       "3. Добавить товар в корзину\n" \
       "4. Удалить товар из корзины\n" \
       "5. Посмотреть корзину\n" \
       "6. Закрыть сайт"

if __name__ == '__main__':
    new_cart = ShoppingCart()
    while True:
        print(MENU)
        command = int(input("Выберите команду: "))

        if command == 1:
            print(Barcode.EAN_13.get_info())

        if command == 2:
            if ShoppingCart.making_order(new_cart):
                print("Заказ оформлен в отдельный файл.")
                break
            else:
                print("Корзина пуста.")

        if command == 3:
            code = input("Введите штрих-код: ")
            print(ShoppingCart.add_good(new_cart, code))

        if command == 4:
            code = input("Введите штрих-код: ")
            print(ShoppingCart.delete_good(new_cart, code))

        if command == 5:
            if new_cart.check_fill():
                for element in new_cart.cart:
                    print(*element)
            else:
                print("Корзина пуста.")

        if command == 6:
            break
