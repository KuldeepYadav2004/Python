price=float(input('enter the price of product:'))
discount=0
if price >= 1000:
    discount=25/100*price
elif price < 1000 and price >= 500:
    discount=10/100*price
else:
    discount=5/100*price

print('discount you got :', discount)
print('amt to pay ;',price-discount)
