age_input = int(input("enter your age:"))
def age_for_vote():
    if age_input>= 16:
        print("you are eligible for vote in Peturksbouipo")
    else:
        print("you are not eligible")
    if age_input >= 25:
        print("you are eligible for vote in Stanlau")
    else:
        print("you are not eligible")
    if age_input >= 48:
        print("you are eligible for vote in Mayengua")
        
    else:
        print("you are not eligible")
age_for_vote()