def temp_convert(degree_frh):
    degree_frh = int(input("enter your temperature in fahrenheit:"))
    degree_calsius = (degree_frh- 32)*5.0/9.0
    print(degree_calsius)
temp_convert(input)