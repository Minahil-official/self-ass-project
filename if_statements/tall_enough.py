munimum_height = 50
def find_height():
    user_height = float(input("enter your height:"))
    if user_height >= munimum_height:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")
find_height()