
# Restaurant scenario: You want to design a program to calculate the bill for a customer's order in a restaurant.
#* Define a base class MenuItem:
#  This class should have attributes like name, price, and a method to calculate the total price.
#* Create subclasses for different types of menu items: 
# Inherit from MenuItem and define properties specific to each type (e.g.,     Beverage, Appetizer, MainCourse).
#* Define an Order class: 
#  This class should have a list of MenuItem objects and methods to add items, calculate the total bill amount, and potentially apply specific discounts based on the order composition.
#* Create a class diagram with all classes and their relationships. 
#* The menu should have at least 10 items. The code should follow PEP8 rules.

class MenuItem:
    def __init__(self,name: str, price: float, description: str = "", x: float = 0) :
        self.name = name
        self.price = price 
        self.discount = x
        self.description = description
    
    def calculate_total_price(self)-> float:
        a = self.price * (1 - self.discount/100)
        self.x = 0 
        return a
    
    def new_discount(self, tacaño)->float:
        if tacaño == 0:
            self.discount = 0
        else:
            self.discount += tacaño


class Dessert(MenuItem):
    def __init__(self, name: str, price: float, gluten: bool, description: str, x: float = 0):
        self.gluten = gluten
        super().__init__(name, price, description, x)
    
    def __str__(self):
        return f"{self.name} (gluten: {self.gluten}): {self.price}, {self.description}"

class MainCourse(MenuItem):
    def __init__(self, name: str, price: float, type: str, description: str, x: float = 0):
        super().__init__(name, price, description, x)
        self.type = type
    
    def __str__(self):
        return f"{self.name} ({self.type}): {self.price}, {self.description}"  

class Beverage(MenuItem):
    def __init__(self, name: str, price: float, brand: str, description: str, x: float = 0):
        super().__init__(name, price, description, x)
        self.brand = brand

    def __str__(self):
        return f"{self.name} - {self.brand}: {self.price}, {self.description}"


class Appetizer(MenuItem):
    def __init__(self, name: str, price: float, cantidad: float, description: str, x: float = 0):
        self.cantidad = cantidad
        super().__init__(name, price, description, x)   

    def __str__(self):
        return f"{self.name} (cantidad: {self.cantidad} gr): {self.price}, {self.description}"

class Order:
    def __init__(self, menu: list, tip: float = 0):
        self.menu = menu
        self.tip = tip
        self.order = []
        self.limit = 0
    
    def see_menu(self):
        n = len(self.menu)
        for i in range(n):
            print(str(i + 1) + ".", self.menu[i])
        return f"{n}. {self.menu[n - 1]}"

    def see_order(self):
        print("")
        n = len(self.order)
        print("lo que has pedido:")
        print("")
        for i in range(n):
            print(f"[{self.order[i].name} - con un descuento de {self.order[i].discount}%]")
        return ""

    
    def add_item(self, food :"MenuItem")-> list:
        self.limit = 0
        for i in self.order:
            i.new_discount(0)
        self.order.append(food)
        return f"se añidio {food.name} (se reiniciaron todos los descuentos)"

    def calculate_bill_amount(self):
        print("")
        amount = 0
        for i in self.order:
            amount += i.calculate_total_price()
        return amount
    
    def cba_tip(self):
        return self.calculate_bill_amount() * (1 + self.tip/100)
         
    def discounts(self):
        print("")
        desserts = [i for i in self.order if isinstance(i, Dessert)]
        main_coursess = [i for i in self.order if isinstance(i, MainCourse)]
        bevereages = [i for i in self.order if isinstance(i, Beverage)]
        appetizers = [i for i in self.order if isinstance(i, Appetizer)]
        if self.calculate_bill_amount() >= 80000:
            for i in self.order:
                i.new_discount(15)
            print("Tu cuenta es mas de 80000, 15% en la cuenta total")
       
        elif len(desserts) + len(main_coursess) + len(bevereages) + len(appetizers) >= 4:
            for i in self.order:
                i.new_discount(20)
            return "por comprar un postre, plato fuerte, aperitivos y postre ahora tiene un 20% de descuento!"
        elif (len(main_coursess) + len(bevereages)) % 2 == 0 :
            for i in self.order:
                if i in main_coursess or i in bevereages:
                    i.new_discount(10)
                else:
                    pass
            return "por comprar cantidades pares de bebidas y de platos fuertes son un 10% mas baratos!"
        elif self.limit >= 0: 
            return "no puedes aplicarle descuento al descuento, bobo hpta"
        else:
            return "no hay descuentos disponibles, pobre"

         
milhoja = Dessert("milhoja", 7500, True, "Postre con mil hojas")
pollo_asado = MainCourse("pollito asado", 40000, "pollo","Un pollo asado de dudosa procedencia")
bistec = MainCourse("bistec", 25000, "carne", "Hecho de las vacas de genetica en la nacional")
natilla = Dessert("natilla", 5000, True, "Delicioso postre colombiano con leche de bufalo")
changua = Appetizer("changua", 9500, 500,"leche con huevo (¿Quien creyo que era buena idea esto?)")
cerveza_1 = Beverage("cerveza", 3500, "poker", "Cerveza que toma el rolo promedio")
aguardiente = Beverage("aguardiente 1/2", 16000, "nectar", "Agua que pica pero rico")
chunchullo = Appetizer("chunchullo", 12000, 200, "No preguntes de donde viene, solo disfrutalo")
mojarra = MainCourse("mojarra", 40000, "pescado","OJO CON LAS ESPINAS")
limonada = Beverage("limonada de coco", 3500, "frutiño", "Limonada hecha con agua de la llave")

menu = [milhoja, pollo_asado, bistec, natilla, changua, cerveza_1, aguardiente, chunchullo, mojarra, limonada]
cliente = Order(menu, tip = 0)
cliente.see_menu()
cliente.add_item(pollo_asado)
cliente.add_item(bistec)
print(cliente.see_order())
print(cliente.calculate_bill_amount())

print(cliente.discounts())
print(cliente.calculate_bill_amount())
cliente.see_order()
print("")
print(cliente.add_item(mojarra))
print(cliente.add_item(milhoja))
print(cliente.add_item(changua))
cliente.see_order()
cliente.calculate_bill_amount()
cliente.discounts()
cliente.see_order()
a = float(input(f"cuanto porcentaje de la cuenta quieres agregar (cuenta actual {cliente.calculate_bill_amount()}): "))
cliente.tip = a
print(f"Total a pagar: {cliente.cba_tip()}, cuenta de {cliente.calculate_bill_amount()} con propina de: {cliente.tip}%" )


