products = [
    ['apple', 10],
    ['orange', 5],
    ['banana', 12],
    ['date', 20],
    ['strawberry', 16]
]


for i, product in enumerate(products):
    print(f"{i} - {product[0]} : ${product[1]}")


choice = int(input("Enter the number of the product you want: "))


if 0 <= choice < len(products):
    name, price = products[choice]


    final_price = price * 1.15

    print(f"Product name: {name}")
    print(f"Price before tax: ${price}")
    print(f"Price after tax: ${final_price}")

else:
    print("Invalid product number ✘")