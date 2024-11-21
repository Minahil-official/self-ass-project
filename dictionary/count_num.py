
def count_number():
  dic = {}
  while True:
    uer_input = (input("enter your number:"))
    if uer_input.lower() =="stop":
      break
    uer_input = int(uer_input)
    if uer_input in dic:
      dic[uer_input] +=1
    else:
      dic[uer_input] =1 
         
  for number, count in dic.items():
    print(f"{number} appears {count} time(s).")
count_number()
