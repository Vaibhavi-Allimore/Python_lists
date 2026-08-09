products=["pen","book","pencil","bag","bottle"]
print("Products:",products)
search=input("Enter product name:")
if search in products:
    print("Product available")
else:
    print("product not available")
