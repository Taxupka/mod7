class Product:

    def __init__(self, name, weight, category): #  Атрибут name - название продукта (строка).
        self.name = name   #Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
        self.weight = weight   #Атрибут category - категория товара (строка).
        self.category = category   #


    def __str__(self):   #Метод __str__, который возвращает строку в формате
        return f'<{self.name}>, <{self.weight}>, <{self.category}>'# <название>, <вес>, <категория>'


class Shop:

    def __init__(self):
        self.__file_name = 'products.txt'
        file = open(self.__file_name, "a")   #Инкапсулированный атрибут


    def get_products(self):
        file = open(self.__file_name, 'r')  #Метод get_products(self), который считывает
        inf = file.read()    #всю информацию из файла __file_name, закрывает его и возвращает
        file.close()    # единую строку со всеми товарами из файла __file_name.
        return inf


    def add(self, *products):
        inf = self.get_products().splitlines()   # присвоение переменной результата работы get_products в виде строки
        file = open(self.__file_name, 'a')   # открытие products.txt

        for i in products:   # Добавляет в файл __file_name каждый продукт из products,
            product = f'{i.name}, {i.weight}, {i.category}'   #если его ещё нет в файле (по названию).
            if product in inf:   # Если такой продукт уже есть, то не добавляет и выводит строку
                print(f'Продукт <{product}> уже есть в магазине')   # 'Продукт <название> уже есть в магазине' .
            else:
                file.write(f'{product}\n')



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())



