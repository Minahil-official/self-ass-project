def count_even():
    li = []
    end = "stop"
    while True:
        numbers = (input("enter your numbers or press enter to stop:"))
        if numbers == end:
            break
        try:
            numbers = int(numbers)
            li.append(numbers)
            if numbers %2 == 0:
               print(f"{numbers} is even")
        except Exception as e:
            print(e)
        print(f"Total even numbers: {(li)}")
count_even()