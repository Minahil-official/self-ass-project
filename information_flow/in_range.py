def in_range(n,low,high):
    if n >=low and n<= high:
        print("n is between low and high ")
    else:
        print("its not between low and high")
n = float(input("enter number:"))
low = float(input("enter number:"))
high = float(input("enter number:"))
in_range(n,low,high)