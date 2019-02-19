sour=int(input("Enter source:"))
dest=int(input("Enter Destination:"))
print("1-auto")
print("2-mini")
print("3-micro")
print("4-prime")
choice=float(input("Enter your choice(1 or 2 or 3 or 4):"))
choice=round(choice)
if choice== 1:
  m=10
  fare=(dest-sour)*m
  print("your fare=",fare)
elif choice== 2:
  m=20
  fare=(dest-sour)*m
  print("your fare=",fare)
elif choice== 3:
  m=50
  fare=(dest-sour)*m
  print("your fare=",fare)  
elif choice== 4:
  m=100
  fare=(dest-sour)*m
  print("your fare=",fare) 
else:
  print("INVALID")   
print("\n\n\t\t--------------------")  
print("\n\t\t\t CAB DETAILS")
print("\n\t\t--------------------")
c=(dest-sour)
print("YOUR TOTAL DISTANCE:Rs.",c)
print("FARE PER KM        :Rs.",m)
print("TOTAL FARE         :Rs.",fare)
print("\n\t\t--------------------")
