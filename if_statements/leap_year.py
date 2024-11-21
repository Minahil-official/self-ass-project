def find_leap_year():
    year_input = int(input("enter your year:"))
    if year_input % 4 == 0:
        if year_input% 100 == 0:
            if year_input %400 == 0:
                print("that's a leap  year")
            else:
                print("that's not a leap year")
        else:
            print("that a leap year")          
    else:
        print("that's not a leap year")        
find_leap_year()