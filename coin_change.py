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

def coin_amount(input):
    print("You have {} in total change".format(input))
    return input

def quarters_left(input):
    quarters = (input // 25)
    change = (input % 25)
    return quarters, change

def dimes_left(input):
    dimes = (input // 10)
    change = (input % 10)
    return dimes, change

def nickel_left(input):
    nickel = (input // 5)
    change = (input % 5)
    return nickel, change

def coint_count(input):
    print(input)
    return input


def main():
    today = date.today()
    d3 = today.strftime("%m/%d/%y")
    chady = Student("Chady Aboulhosn", "NO Class","Coin Change" , d3)
    chady.show()

    exact_amount = coin_amount(int(input('Enter in exact change : \n')))

    quarters, exact_amount = quarters_left(exact_amount)

    dimes, exact_amount = dimes_left(exact_amount)
    # nickels, exact_amount = nickel_left(exact_amount)

    pennies = exact_amount

    # sum = pennies + dimes + nickels + quarters
    sum = pennies + dimes  + quarters

    print("You have {} quarters as change".format(quarters))
    print("You have {} dimes as change".format(dimes))
    # print("You have {} nickels as change".format(nickels))
    print("You have {} pennies as change".format(pennies))

    print("total number of coins is {} ".format(sum))





if __name__== "__main__":
  main()