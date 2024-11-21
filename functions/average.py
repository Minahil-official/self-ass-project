def cal_average():
    li = []
    num1 = float(input("enter your number:"))
    num2 = float(input("enter your number:"))
    li.append(num1)
    li.append(num2)
    average = sum(li)/len(li)
    print(average)
cal_average()
        
         #OR
def average():
    num1 = float(input("enter your number:"))
    num2 = float(input("enter your number:"))
    my_average = (num1+num2)/2
    print(my_average)
average()