fruits = {'apple':20,'banana':10,'orange':15,'cherry':45}
def pop_up_shop():
    total = 0
    for fruit,price in fruits.items():
        try:
           choose = int(input(f"how much {fruit}s do you want:"))
           total+=choose*price
        except ValueError as e:
            print(e)
        print(f"the total price is {total}")
pop_up_shop()
            
        
    