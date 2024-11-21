import math
def pythagorean():
    length_of_AB = float(input("enter the length of AB:"))
    length_of_Ac =float(input("enter the length of AC:"))
    length_of_BC = math.sqrt(length_of_AB**2+length_of_Ac**2)
    print(f"the lenght of BC is {length_of_BC}")
pythagorean()