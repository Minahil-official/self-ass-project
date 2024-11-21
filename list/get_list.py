def get_list():
    my_list = []
    count = 0
    while count<3: 
        num = int(input('enter your number:'))
        my_list.append(num)
        print(f"here is your lis{my_list}")
        count+=1
        
get_list()