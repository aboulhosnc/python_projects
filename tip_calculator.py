


def tip_calulator(total, people, tip):
    tip = tip / 100
    total = total / people
    tip_amount = total * tip
    new_total = total + tip_amount

    return tip_amount, new_total
    # pass


def main():
    print('hello')

    go_condition = True
    
    while go_condition:
        total = float(input('Enter in the amount : '))
        people_num = int(input('Enter in the total amount of people : '))
        tip = float(input('Enter in the tip percentage you want : '))

        tip_amount, new_total = tip_calulator(total,people_num,tip)

        print('Tip for each person  is {} \n Total Bill equals {}'.format(tip_amount, (new_total * people_num)))

        go_condition = (input('Enter False to stop'))



if __name__== "__main__":
  main()