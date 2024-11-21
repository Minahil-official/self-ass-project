def num_in_stock(fruit):
    if fruit == "apple":
        return 2
    elif fruit == "orange":
        return 10
    elif fruit == "lichey":
        return 1000
    else:
        return 0
fruit = input("enter a fruit:")
print(num_in_stock(fruit))