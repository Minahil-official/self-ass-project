def phone_book():
    dic = {}
    while True:
        names = input("Enter your name (or 'stop' to finish):")
        if names.lower() == "stop":
            break
        dic[names] = None  # Initialize entry for the name

    for names in dic:
        while True:
            num = (input(f"Enter the number for {names} (or 'finish' to stop):"))
            if num == "finish":
                break
            try: 
                num = int(num)
                dic[names] = num
                break

            except Exception as e:
            
                print(e)
    print("phone_book")            
    for names,numbers in dic.items():
        print(f"{names}:{numbers}")
         
phone_book()


