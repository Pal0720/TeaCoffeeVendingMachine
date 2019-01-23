from abc import ABCMeta
import sys
import time
import datetime

#######################################
class Container(object):

    __metaclass__ = ABCMeta

    def check_container_status(self):
        return self.capacity


class Raw_tea(Container):

    def __init__(self):
        self.capacity = 2000

    def refill_capacity(self):
        self.capacity = 2000

    def get_tea_material(self, quantity):
        self.capacity -= (5 * quantity)

    def get_black_tea_material(self, quantity):
        self.capacity -= (3 * quantity)


class Raw_coffee(Container):

    def __init__(self):
        self.capacity = 2000

    def refill_capacity(self):
        self.capacity = 2000

    def get_coffee_material(self,quantity):
        self.capacity -= (4 * quantity)


    def get_black_coffee_material(self, quantity):
        self.capacity -= (3 * quantity)


class Sugar_container(Container):

    def __init__(self):
        self.capacity = 8000

    def refill_capacity(self):
        self.capacity = 8000

    def sugar_for_tea(self,quantity):
        self.capacity -= (15 * quantity)

    def sugar_for_black_tea(self,quantity):
        self.capacity -= (15* quantity)

    def sugar_for_coffee(self, quantity):
        self.capacity -= (15* quantity)

    def sugar_for_black_coffee(self,quantity):
        self.capacity -= (15 * quantity)


class Milk_container(Container):

    def __init__(self):
        self.capacity = 10000

    def refill_capacity(self):
        self.capacity = 10000

    def milk_for_tea(self, quantity):
        self.capacity -= (40 * quantity)

    def milk_for_coffee(self, quantity):
        self.capacity -= (80 * quantity)


class Water_container(Container):

    def __init__(self):
        self.capacity = 15000

    def refill_capacity(self):
        self.capacity = 15000

    def water_for_tea(self,quantity):
        self.capacity -= (60 *quantity)

    def water_for_black_tea(self,quantity):
        self.capacity -= (100 *quantity)

    def water_for_coffee(self,quantity):
        self.capacity -= (20*quantity)

    def water_for_black_coffee(self, quantity):
        self.capacity -= (100 *quantity)

###########################################################################################################
class Machine:

    @staticmethod
    def show_menu():
        print("******************************************************")
        print("Menu :\n1) Tea\t\t10 Rs.\n2) Black Tea\t5 Rs\n3) Coffee\t15 Rs.\n4) Black Coffee\t10 Rs\n")

    def __init__(self):
        self.containers = []
        self.build()
        print("Machine is ready to take your orders..!!")

    def build(self):
        self.containers.extend((Raw_tea(),Raw_coffee(),Sugar_container(),Milk_container(),Water_container()))

    def make_tea(self,quantity):
        if self.containers[0].capacity<(5*quantity) or self.containers[2].capacity<(15*quantity) or self.containers[3].capacity<(40*quantity) or self.containers[4].capacity<(60*quantity):
            print("Not enough material.. Please refill")
        else :
            amount = 10 * quantity
            self.containers[0].get_tea_material(quantity)
            self.containers[2].sugar_for_tea(quantity)
            self.containers[3].milk_for_tea(quantity)
            self.containers[4].water_for_tea(quantity)
            print("{} tea prepared. Total amount is {}".format(quantity, amount))

    def make_coffee(self,quantity):
        if self.containers[1].capacity<(4*quantity) or self.containers[2].capacity<(15*quantity) or self.containers[3].capacity<(80*quantity) or self.containers[4].capacity<(20*quantity):
            print("Not enough material.. Please refill")
        else:
            amount = (15 * quantity)
            self.containers[1].get_coffee_material(quantity)
            self.containers[2].sugar_for_coffee(quantity)
            self.containers[3].milk_for_coffee(quantity)
            self.containers[4].water_for_coffee(quantity)
            print("{} Coffee prepared. Total amount is {}".format(quantity, amount ))

    def make_black_coffee(self,quantity):
        if self.containers[1].capacity<(3*quantity) or self.containers[2].capacity<(15*quantity) or self.containers[4].capacity<(60*quantity):
            print("Not enough material.. Please refill")
        else:
            amount = 10*quantity
            self.containers[1].get_black_coffee_material(quantity)
            self.containers[2].sugar_for_black_coffee(quantity)
            self.containers[4].water_for_black_coffee(quantity)
            print("{} Black coffee prepared. Total amount is {}".format(quantity,amount))

    def make_black_tea(self,quantity):
        if self.containers[0].capacity<(3*quantity) or self.containers[2].capacity<(15*quantity) or self.containers[4].capacity<(100*quantity):
            print("Not enough material.. Please refill")
        else:
            amount = (5 * quantity)
            self.containers[0].get_black_tea_material(quantity)
            self.containers[2].sugar_for_black_tea(quantity)
            self.containers[4].water_for_black_tea(quantity)
            print("{} Black tea prepared. Total amount is {}".format(quantity,amount))



######################################
########################################

def exit():
    print("Thank you..! Visit again..!")
    sys.exit()


def preparing():
    print("Your order is being prepared..")
    for i in range(3):
        print("...",end = '')
        time.sleep(1)
    print("Here is your order ")


def refilling():
    print("Refilling containers..")
    for i in range(3):
        print("...",end = '')
        time.sleep(1)
    print("Containers refilled.. You can order now..!!")


def check_sales(orders):
    sales = 0
    for i in orders:
        sales += i["Amount"]
    return sales


###########################################################
#########################################

print("**************************************")
print("Welcome to the Vending Machine..!")
print("**************************************")
print("What do you want to do today??")
print("**************************************")
print()


#orders = {"Tea":[],"Black Tea":[],"Coffee":[],"Black coffee":[]}
Tea_orders = []
Coffee_orders = []
Black_tea_orders = []
Black_coffee_orders = []

# build the machine, with full capacity
machine = Machine()

while(True):
    print("******************************************************")
    choice = str(input("1) Order\n2) Check container status\n3) Refill Container\n4) Show orders\n5) Check Sales\n6) Exit\nYour choice : "))

    if choice == '1':
        Machine.show_menu()
        choice_menu = input("What do you want to order : ")
        quantity = int(input("How many : "))
        if choice_menu == "1":
            preparing()
            machine.make_tea(quantity)
            Tea_orders.append({"Date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"quantity" : quantity, "Amount": (10*quantity)})
        elif choice_menu =='2':
            preparing()
            machine.make_black_tea(quantity)
            Black_tea_orders.append({"Date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"quantity" : quantity, "Amount": (5*quantity)})
        elif choice_menu =='3':
            preparing()
            machine.make_coffee(quantity)
            Coffee_orders.append({"Date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"quantity" : quantity, "Amount": (15*quantity)})
        elif choice_menu == '4':
            preparing()
            machine.make_black_coffee(quantity)
            Black_coffee_orders.append({"Date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"quantity" : quantity, "Amount": (10*quantity)})
        else:
            print("Oops.. Please select from the available menu!")

    elif choice == '2':
        print("Tea container remaining material : {} mg".format(machine.containers[0].check_container_status()))
        print("Coffee container remaining material : {} mg".format(machine.containers[1].check_container_status()))
        print("Sugar container remaining material : {} mg".format(machine.containers[2].check_container_status()))
        print("Milk container remaining material : {} ml".format(machine.containers[3].check_container_status()))
        print("Water container remaining material : {} ml".format(machine.containers[4].check_container_status()))

    elif choice == '3':
        refilling()
        machine.containers[0].refill_capacity()
        machine.containers[1].refill_capacity()
        machine.containers[2].refill_capacity()
        machine.containers[3].refill_capacity()
        machine.containers[4].refill_capacity()

    elif choice == '4':
        print("Here are the previous orders :")
        if len(Tea_orders)>0:
            print("Tea : {}".format(Tea_orders))
        if len(Black_tea_orders)> 0:
            print("Black Tea : {}".format(Black_tea_orders))
        if len(Coffee_orders)>0:
            print("Coffee : {}".format(Coffee_orders))
        if len(Black_coffee_orders)>0:
            print("Black coffee : {}".format(Black_coffee_orders))

    elif choice == '5':
        print("******************************************************")
        print("Total machine sales : {} Rs".format(check_sales(Tea_orders)+check_sales(Black_tea_orders)+check_sales(Coffee_orders)+check_sales(Black_coffee_orders)))
        print("Total sales for Tea  : {} Rs".format(check_sales(Tea_orders)))
        print("Total sales for Black Tea  : {} Rs".format(check_sales(Black_tea_orders)))
        print("Total sales for Coffee  : {} Rs".format(check_sales(Coffee_orders)))
        print("Total sales for Black coffee  : {} Rs".format(check_sales(Black_coffee_orders)))

    elif choice == '6':
        exit()
