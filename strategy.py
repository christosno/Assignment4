import abc
from enum import Enum


colors = {
    1 : {'name' : 'RED', 'price' : 5},
    2 : {'name' : 'ORANGE', 'price' : 7},
    3 : {'name' : 'YELLOW', 'price' : 7},
    4 : {'name' : 'GREEN', 'price' : 5},
    5 : {'name' : 'BLUE', 'price' : 5},
    6 : {'name' : 'INDIGO', 'price' : 7},
    7 : {'name' : 'VIOLET', 'price' : 7},
}

sizes = {
    1 : {'name' : 'XS', 'price' : 5},
    2 : {'name' : 'S', 'price' : 6},
    3 : {'name' : 'M', 'price' : 7},
    4 : {'name' : 'XL', 'price' : 8},
    5 : {'name' : 'XXL', 'price' : 9},
    6 : {'name' : 'XXXL', 'price' : 10},
}

fabrics = {
    1 : {'name' : 'WOOL', 'price' : 15},
    2 : {'name' : 'COTTON', 'price' : 15},
    3 : {'name' : 'POLYESTER', 'price' : 10},
    4 : {'name' : 'RAYON', 'price' : 15},
    5 : {'name' : 'LINEN', 'price' : 15},
    6 : {'name' : 'CASHMERE', 'price' : 20},
    7 : {'name' : 'SILK', 'price' : 15},
}

class T_shirt:

    def __init__(self, color, size, fabric):
        self.color = color
        self.size = size
        self.fabric = fabric
        self.colorName = colors[color]['name']
        self.sizeName = sizes[size]['name']
        self.fabricName = fabrics[fabric]['name']
        self.price = colors[color]['price'] + sizes[size]['price'] + fabrics[fabric]['price']

        # for the size, color, fabric sorting
        li = [self.size, self.color, self.fabric]
        string_ints = [str(int) for int in li]
        str_of_ints = ''.join(string_ints)
        self.sizeColorFabric = int(str_of_ints)
       

    def __str__(self):
        return "T-shirst with:\n\t Size : {},\n\t Color : {},\n\t Fabric : {},\n\t Price : {}".format(self.sizeName, self.colorName, self.fabricName, self.price)


class PaymentMethodStrategy(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def paymentMethod(self, price):
        pass

class CreditDepitMethod(PaymentMethodStrategy):

    def paymentMethod(self, price):
        print("The payment method for {}$ is Credit / Depit!".format(price))

class MoneyBankMethod(PaymentMethodStrategy):

    def paymentMethod(self, price):
        print("The payment method for {}$ is Money / Bank!".format(price))

class CashMethod(PaymentMethodStrategy):

    def paymentMethod(self, price):
        print("The payment method for {}$ is Cash!".format(price))

class Context:

    def __init__(self, strategy=CashMethod()):
        self.strategy = strategy

    def executeStrategy(self, price):
        return self.strategy.paymentMethod(price)


if __name__=="__main__":
    
    # prints the main menu and returns our selection
    def Main_Menu():
        print("\t\t~ MAIN MENU ~")
        print()
        choice = input("\tDo you need something else?\n\t0: Yes\n\t1: No\n\t ->")
        while choice not in ["0","1"]:
            print("Sorry, i don't understand")
            print("Please chose again: 0 for Yes , 1 for No")
            choice = input("\tDo you need something else?\t0: Yes\n\t1: No\n\t ->")

        return choice

    def Color_Choice():
        print("\t\t~ Chouse the color ~")
        print()
        choice = input("\t1: RED\n\t2: ORANGE\n\t3: YELLOW\n\t4: GREEN\n\t5: BLUE\n\t6: INDIGO\n\t7: VIOLET\n\t ->")
        while choice not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("Sorry, i don't understand")
            print("Please chose again color")
            choice = input("\t1: RED\n\t2: ORANGE\n\t3: YELLOW\n\t4: GREEN\n\t5: BLUE\n\t6: INDIGO\n\t7: VIOLET\n\t ->")

        return int(choice)

    def Size_Choice():
        print("\t\t~ Chouse the size ~")
        print()
        choice = input("\t1: XS\n\t2: S\n\t3: M\n\t4: XL\n\t5: XXL\n\t6: XXXL\n\t ->")
        while choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Sorry, i don't understand")
            print("Please chose again size")
            choice = input("\t1: XS\n\t2: S\n\t3: M\n\t4: XL\n\t5: XXL\n\t6: XXXL\n\t ->")

        return int(choice)

    def Fabric_Choice():
        print("\t\t~ Chouse the fabric ~")
        print()
        choice = input("\t1: WOOL\n\t2: COTTON\n\t3: POLIESTER\n\t4: RAYON\n\t5: LINEN\n\t6: CASHMIRE\n\t7: SILK\n\t ->")
        while choice not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("Sorry, i don't understand")
            print("Please chose again fabric")
            choice = input("\t1: WOOL\n\t2: COTTON\n\t3: POLIESTER\n\t4: RAYON\n\t5: LINEN\n\t6: CASHMIRE\n\t7: SILK\n\t ->")

        return int(choice)

    def Strategy_Choice():
        print("\t\t~ Chouse the payment method ~")
        print()
        choice = input("\t1: Credit / Depit\n\t2: Money / Bank\n\t3: Cash\n\t ->")
        while choice not in ["1", "2", "3"]:
            print("Sorry, i don't understand")
            print("Please chose again payment method")
            choice = input("\t1: Credit / Depit\n\t2: Money / Bank\n\t3: Cash\n\t ->")

        return choice

    MainMenuChoice = None
    SizeChoice = None
    ColorChoice = None
    FabricChoice = None
    PaymentMethod = None
    t_shirt_list = []
    total_price = 0

    while MainMenuChoice != '1':

        SizeChoice = Size_Choice()
        ColorChoice = Color_Choice()
        FabricChoice = Fabric_Choice()

        t_shirt = T_shirt(ColorChoice, SizeChoice, FabricChoice)
        t_shirt_list.append(t_shirt)

        MainMenuChoice = Main_Menu()


    print('The order is:')

    for t_shirt in t_shirt_list:
        print('~ {}, {}, {} T-shirt with price {}$'.format(t_shirt.colorName, t_shirt.sizeName, t_shirt.fabricName, t_shirt.price))
        total_price += t_shirt.price
    print()
    print('The total cost is {}$'.format(total_price))
    PaymentMethod = Strategy_Choice()
    
    if PaymentMethod == '1':
        contex = Context(CreditDepitMethod())
        contex.executeStrategy(total_price)
    elif PaymentMethod == '2':
        contex = Context(MoneyBankMethod())
        contex.executeStrategy(total_price)
    else:
        contex = Context(CashMethod())
        contex.executeStrategy(total_price)
