shopping_cart=[]
for i in range(1,5):
    product_price=int(input("Enter product price:"))
    shopping_cart.append(product_price)
print(shopping_cart)
total=sum(shopping_cart)
print("Total cart value:",total)
expensive=max(shopping_cart)
print("Expensive price: ",expensive)
count=len(shopping_cart)
print("Number of  item ",count)
remove=int(input("Enter price to remove:"))
shopping_cart.remove(remove)
print("Removes an  item ",shopping_cart)


    
