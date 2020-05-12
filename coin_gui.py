from tkinter import *
master = Tk()
Label(master, text='First Name', font = ('Courier', 22)).grid(row=0)
Label(master, text='Last Name').grid(row=1)
Label(master, text='Answer').grid(row=2)


e1 = Entry(master)
e2 = Entry(master)
answer = e1
Label(master, text = answer).grid(row=2, column = 1)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
# e3.grid(row=2, column=1)
mainloop()

# def min_coins_dp(cents):
#     num_of_coins = [0] * (cents + 1)
#     num_of_coins[0] = 0
#     coins = [25, 10, 1]
#     for i in range(1, cents + 1):
#         temp = cents + 1
#         for j in coins:
#             coins_j =  i / j
#             if coins_j != 0:
#                 temp = min(temp, coins_j + num_of_coins[cents - coins_j * j])
#         num_of_coins[i] = temp
#     return num_of_coins[cents]
#
# # print(num_of_coins)
# print (min_coins_dp(31))
# print (min_coins_dp(70))
