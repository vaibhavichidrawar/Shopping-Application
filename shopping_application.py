#SHOPPING APPLICATION

print("Welcome to the Shopping Application")

print("""
    1.Electronics
    2.Clothing
    3.grocery
    4.Exit 
      """)

choice=int(input("Enter Your Choice: "))

if choice==1:
  print("""
        1.Mobile (25000Rs)
        2.TV     (15000Rs)
        3.Laptop (100000Rs)
        4.Exit
          """)
  choice1=int(input("Enter Your Choice: "))
  if choice1==1:
    price=25000
    print("You have selected mobile")
    print("Price:",price)
  elif choice1==2:
    price=15000
    print("You have selected Tv")
    print("Price:",price)
  elif choice1==3:
    price=100000
    print("You have selected Laptop")
    print("Price:",price)
  elif choice1==4:
    print("Thank You For Visitng")
  else:
    print("Invalid choice")

elif choice==2:
  print("""
        1.Shirt (1000Rs)
        2.Pant  (2000Rs)
        3.Saree (5000Rs)
        4.Exit
       """)
  choice2=int(input("Enter Your Choice:"))
  if choice2==1:
    price=1000
    print("You have selected shirt")
    print("Price:",price)
  elif choice2==2:
    price=2000
    print("You have selected pant")
    print("Price:",price)
  elif choice2==3:
    price=5000
    print("You have selected saree")
    print("Price:",price)
  elif choice2==4:
    print("Thank You For Visiting")
  else:
    print("Invalid Choice")

elif choice==3:
  print("""
        1.Sugar (38Rs)
        2.Oil   (130Rs)
        3.Nirma (60Rs)
        4.Exit
        """)  
  choice3=int(input("Enter Your choice:"))
  if choice3==1:
    price=38
    print("You have selected Sugar")
    print("Price:",price)
  elif choice3==2:
    price=130
    print("You have selected Oil")
    print("Price:",price)
  elif choice3==3:
    price=60
    print("You have selected")
    print("Price:",price)
  elif choice3==4:
    print("Thank You For visiting")
  else:
    print("Invalid Choice")

elif choice==4:
  print("Thank You For Visiting")

else:
  print("Invalid Choice")

quantity=int(input("Enter the quantity: "))
total=price*quantity

if total>30000:
  discount=total*0.20
  print("You have got 20% discount")
elif total>15000:
  discount=total*0.10
  print("You have got 10% discount")
else:
  discount=0
  print("No Discount")

finalamount=total-discount
print("Your final amount is :",finalamount)
print("You Got Discount: Rs",discount)
print("DO VISIT AGAIN...❤️")