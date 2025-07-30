price=float(input('enter the price of the product :'))
discount=0
if price >= 500:
    discount=10/100*price
else:
    discount=5/100*price

print('discount you got:',discount)
print('amount to pay :',price -discount)
