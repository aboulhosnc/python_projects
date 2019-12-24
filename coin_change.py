from datetime import date

class Student():

    def __init__ (self,user_name,class_number,assignment, date, class_title = "",class_name = ""):
        self.user_name = user_name
        self.class_number = class_number
        self.assignment = assignment
        self.date = date
        self.class_title = class_title
        self.class_name = class_name

    def show(self):
        print("..........................................")
        print("Name   : {}".format(self.user_name))
        print("Class  : {}".format(self.class_number))
        print("Assign : {}".format(self.assignment))
        print("Date   : {}".format(self.date))
        print("..........................................")




#goal is to minimize coins

def coin_amount(exact_amount, order_list):
    print("You have {} in total change".format(exact_amount))

    for i in order_list:
        if(order_list[i] == 1):
            quarters, exact_amount = quarters_left(exact_amount)
        if(order_list[i] == 2):
            dimes, exact_amount = dimes_left(exact_amount)
        # if(order_list[i] == 3):
            # nickels, exact_amount = nickel_left(exact_amount)

        if(order_list[i] == 0):
            pennies = pennies_left(exact_amount)

    # sum = pennies + dimes + nickels + quarters
    sum = pennies + dimes  + quarters
    return sum

def quarters_left(input):
    quarters = (input // 25)
    change = (input % 25)
    print("You have {} quarters as change".format(quarters))
    return quarters, change

def dimes_left(input):
    dimes = (input // 10)
    change = (input % 10)
    print("You have {} dimes as change".format(dimes))
    return dimes, change

def nickel_left(input):
    nickels = (input // 5)
    change = (input % 5)
    print("You have {} nickels as change".format(nickels))
    return nickels, change

def pennies_left(input):
    pennies = input
    print("You have {} pennies as change".format(pennies))
    return pennies

def coint_count(input):
    print(input)
    return input


def main():
    today = date.today()
    d3 = today.strftime("%m/%d/%y")
    chady = Student("Chady Aboulhosn", "NO Class","Coin Change" , d3)
    chady.show()

    exact_amount = (int(input('Enter in exact change : \n') ))
    sum = []
    order_list = []
    for i in range (4):
        order_list = [(i + 1) % 4, (i + 2) % 4, (i + 3) % 4, (i + 4) % 4 ]
        sum.append( coin_amount(exact_amount, order_list))
        # print(order_list)


    # test_1 = 1 % 4
    # test_2 = 2 % 4
    # test_3 = 3 % 4
    # test_4 = 4 % 4
    # # test_0 = 4 % 0
    #
    # # print(test_0)
    # print(test_1)
    # print(test_2)
    # print(test_3)
    # print(test_4)


    # pennies = exact_amount








    print("total number of coins is {} ".format(min(sum)))





if __name__== "__main__":
  main()
