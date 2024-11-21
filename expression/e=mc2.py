c:int = 299792458 #
def mc2():
  m = float(input("enter your mass(in kg):"))
  energy_in_joules: float = m*(c**2)

  print("e= m*c**2")
  print("c = "+str(c)+"m/s" )
  print("m= "+str(m)+"kg")
  print(str(energy_in_joules) + " joules of energy!")
mc2()
  
print(mc2())

c= 299792458 
m = float(input("enter your mass(in kg):"))
e = m*c**2
print(e)



