# price = 1000000
# gd_credit = 10/100 * price
# bd_credit = 20/100 * price
# is_good = False
# if is_good:
#     print('down payment is:' + str(gd_credit))
# else:
#     print('down payment is:' + str(bd_credit))

# using formatted string
price = 1000000
is_good = True
if is_good:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

print(f"down payment is: {down_payment}")