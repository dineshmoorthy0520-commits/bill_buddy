print("=== BILL BUDDY ===")
customer=input("Enter your name:")

# item and the prices
item1=input("Enter a item:")
price1=float(input("Enter a price:"))
item2=input("Enter a item:")
price2=float(input("Enter a price:"))
item3=input("Enter a item:")
price3=float(input("Enter a price:"))

#total and discount
total = price1+price2+price3
if total>=2000:
    discount= total*0.15
elif total>=1000:
    discount= total*0.10
else:
    discount=0
final_amount= total - discount

#billing 
print("===BILL AMOUNT===")
print("Customer Name:",customer)
print("-----------------------")
print(f"item1: ${price1}")
print(f"item2: ${price2}")
print(f"item3: ${price3}")
print("TOTAL:", total)
print("DISCOUNT:", discount)
print(f"final_amount: ${final_amount}")
